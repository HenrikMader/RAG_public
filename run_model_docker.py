import gradio as gr
import chromadb
import os
from chromadb.utils import embedding_functions
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import time
import re
from sentence_transformers import CrossEncoder
from openai import OpenAI

client = OpenAI(base_url="http://vllm:8000/v1", api_key="not-needed")






sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")
reranker = CrossEncoder("jinaai/jina-reranker-v2-base-multilingual", trust_remote_code=True)

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./db")

# Initialize LLaMA model with llama-cpp-python (local model)

#model = SentenceTransformer('all-mpnet-base-v2')
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

MAX_PORT_NUMBER = 65_535

# Function to retrieve relevant documents from ChromaDB
def retrieve_documents(query, collection_name, top_k=20):
 
    collection = chroma_client.get_collection(name=collection_name, embedding_function=sentence_transformer_ef)
    
    #query_embedding = model.encode([query])[0]

    # Perform similarity search with ChromaDB
    results = collection.query(query_texts=[query], n_results=top_k)
    
    # Extract the documents
    retrieved_documents = results["documents"] [0]

    return retrieved_documents


def rerank_documents(query, documents, top_k=5):
    pairs = [(query, doc) for doc in documents]
    scores = reranker.predict(pairs)
    scored_docs = list(zip(documents, scores))
    ranked = sorted(scored_docs, key=lambda x: x[1], reverse=True)
    top_documents = [doc for doc, score in ranked[:top_k]]
    return top_documents


def generate_response_two(query, collection_name, chat_history):
    documents = retrieve_documents(query, collection_name)
    top_documents = rerank_documents(query, documents, top_k=3)

    context = "\n".join(
        f"--------- Chunk {i+1}:\n{doc}\n"
        for i, doc in enumerate(top_documents)
    )

    prompt = f"""
    ### DOCUMENTS:
    {context}

    ### QUERY:
    {query}

    You are a Retrieval Augmented Generation Chatbot (RAG).
    Answer the users QUERY using the DOCUMENTS above.
    If you can not find an Answer to the QUERY in the DOCUMENTS, then use your internal knowledge.

    ### Answer:
    """

    # Make sure the model name is correct
    response = client.chat.completions.create(
        model="ibm-granite/granite-3.3-2b-instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        temperature=0.7,
        stream=True,  # keep streaming
    )

    cmData = ""
    for chunk in response:  # streamed chunks
        if len(chunk.choices) > 0:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                cmData += delta.content

                # Yield updated chat history for Gradio streaming
                partial_history = [(query, cmData)]
                helper = chat_history + [(query, cmData)]
                yield "", partial_history, helper, gr.Textbox.update(value=context, visible=True)

    # Return final chat history
    final_history = chat_history + [(query, cmData)]
    return "", final_history, final_history



# Create Gradio UI
def main():
    # Custom CSS to approximate a ChatGPT look-and-feel
    custom_css = """
    /* Basic background and container styling */
    .gradio-container {
        font-family: Arial, sans-serif;
        background-color: #f5f7f9;
    }
    /* Chatbot messages styling */
    #chatbot .wrap .user {
        background-color: #d1e3ff; /* Light blue bubble for user */
        color: #000;
        border-radius: 8px;
    }
    #chatbot .wrap .bot {
        background-color: #ffffff; /* White bubble for bot */
        color: #000;
        border-radius: 8px;
    }
    /* Remove the standard border from input boxes */
    #chatbot .wrap input {
        border: none !important;
    }
    """

    with gr.Blocks() as demo:
        gr.Markdown("# Chatbot about IBM RedBooks running on IBM POWER10")

        # A hidden state to store the chat hi:wq story (list of (user, bot) tuples).
        chat_history = gr.State([])
        choices = set()

        with open("database_setup.txt", "r") as f:
            for line in f:
                line = line.strip()
                if ":" in line:
                    prefix = line.split(":")[0]  # Normalize case
                    choices.add(prefix)
        
        print(list(choices))

        with gr.Row():
            # Our Chatbot display
            chatbot = gr.Chatbot(
                label="Chatbot",
                elem_id="chatbot",
                height=400
            ).style(container=True)
        with gr.Row():
            retreival_vector_db = gr.Textbox(
                lines = 8,
                interactive=False,
                visible=False,
                label="Source from Documents in Vector DB"
            )

        with gr.Row():
            # User input
            query_input = gr.Textbox(
                show_label=False, 
                placeholder="Enter your query here...",
                container=False
            )

            file_selector = gr.Dropdown(
                label="Which POWER Topic?",
                choices=choices
            )

            # Submit button
            
        with gr.Row():
            submit_button = gr.Button("Submit")

        # When the user clicks "Submit", call generate_response:
        # - Inputs: query_input, file_selector, use_context_toggle, and chat_history
        # - Outputs: (1) cleared query_input, (2) updated chat_history -> displayed by chatbot
        submit_button.click(
            fn=generate_response_two,
            inputs=[query_input, file_selector, chat_history],
            outputs=[query_input, chatbot, chat_history, retreival_vector_db]  # chatbot auto-displays chat_history
        )
    server_port = int(os.getenv("RAG_PORT", "7680"))
    if not (1 <= server_port <= MAX_PORT_NUMBER):
        raise ValueError(
        f"PORT {server_port} outside of valid port Range 1-{MAX_PORT_NUMBER}!"
    )
    # Launch the Gradio app
    demo.launch(server_name="0.0.0.0", server_port = server_port, enable_queue=True)

if __name__ == "__main__":
    main()
