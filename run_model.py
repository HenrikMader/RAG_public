import gradio as gr
import chromadb
from llama_cpp import Llama
import os
from chromadb.utils import embedding_functions
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import time

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./db")

# Initialize LLaMA model with llama-cpp-python (local model)
llama_model_path = os.getenv("RAG_MODEL_PATH") or "model:path"  # Path to your LLaMA model
llama = Llama(model_path=llama_model_path, n_ctx=0)

#model = SentenceTransformer('all-mpnet-base-v2')
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

# Function to retrieve relevant documents from ChromaDB
def retrieve_documents(query, collection_name, top_k=2):
 
    collection = chroma_client.get_collection(name=collection_name, embedding_function=sentence_transformer_ef)
    
    #query_embedding = model.encode([query])[0]

    # Perform similarity search with ChromaDB
    results = collection.query(query_texts=[query], n_results=top_k)
    
    # Extract the documents
    retrieved_documents = results["documents"]
    return retrieved_documents

# Function to generate response with LLaMA model using llama-cpp-python
def generate_response(query, collection_name, chat_history):
    """
    Generates a response from the LLaMA model, using streaming, 
    and updates the chat_history with partial bot outputs.
    """
    
    print("collection")
    print(collection_name)
    if (collection_name == "Openshift/AI on POWER"):
        collection_name = "Openshift"
    elif (collection_name == "Ansible"):
        collection_name = "Ansible"
    else:
        collection_name = "POWER10"

    # You might decide whether to use context (RAG) based on a checkbox or some external setting:
    use_context = True

    if use_context:
        documents = retrieve_documents(query, collection_name)
        print(documents)
        flat_documents = [item for sublist in documents for item in sublist]
        context = "\n".join(flat_documents)

        # -- Optionally, incorporate chat_history so far into the prompt:
        # For a multi-turn conversation, you might do something like:
        # conversation_str = ""
        # for (old_user, old_bot) in chat_history:
        #     conversation_str += f"User: {old_user}\nAssistant: {old_bot}\n"

        # Here, we’ll just demonstrate merging the new context + query:
        input_text = f"""
Query:
{context}

Question:
{query}

Instructions:
Compose a comprehensive reply to the query using the search results given.
Only answer what is asked. If you do not find the answer in the context then state that you do not know.
Answer:
"""
    else:
        # If not using context, just pass the user query
        input_text = f"Query: {query}\nAnswer: "

    # Prepare a string to accumulate the model’s streamed tokens
    cmData = ""

    # Stream tokens from llama(...)
    for output in llama(input_text, max_tokens=4096, stream=True):
        token_text = output['choices'][0]['text']

        # You might skip certain tokens like pure newlines

        cmData += token_text

        # Each time we get new tokens, we yield an updated chat history:
        #   The user’s question is `query`
        #   The partial answer so far is `cmData`
        partial_history = chat_history + [(query, cmData)]

        # By yielding `("", partial_history)`, 
        # - the Textbox input is cleared (set to ""), 
        # - the Chatbot is updated with the new partial history.
        yield "", partial_history

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

    with gr.Blocks(css=custom_css) as demo:
        gr.Markdown("# Chatbot about IBM RedBooks running on IBM POWER10")

        # A hidden state to store the chat history (list of (user, bot) tuples).
        chat_history = gr.State([])

        with gr.Row():
            # Our Chatbot display
            chatbot = gr.Chatbot(
                label="Chatbot",
                elem_id="chatbot",
                height=400
            ).style(container=True)

        with gr.Row():
            # User input
            query_input = gr.Textbox(
                show_label=False, 
                placeholder="Enter your query here...",
                container=False
            )

            file_selector = gr.Dropdown(
                label="Which POWER Topic?",
                choices=["POWER10 Generation", "Openshift/AI on POWER", "Ansible"]
            )

            # Submit button
            
        with gr.Row():
            submit_button = gr.Button("Submit")

        # When the user clicks "Submit", call generate_response:
        # - Inputs: query_input, file_selector, use_context_toggle, and chat_history
        # - Outputs: (1) cleared query_input, (2) updated chat_history -> displayed by chatbot
        submit_button.click(
            fn=generate_response,
            inputs=[query_input, file_selector, chat_history],
            outputs=[query_input, chatbot]  # chatbot auto-displays chat_history
        )

    # Launch the Gradio app
    demo.launch(server_name="0.0.0.0", server_port = 8082, enable_queue=True)

if __name__ == "__main__":
    main()
