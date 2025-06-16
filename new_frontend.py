import os
import gradio as gr
import chromadb
from llama_cpp import Llama
from chromadb.utils import embedding_functions
from theme import IBMTheme

# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./db")

# Initialize SentenceTransformer embedding function
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

# Load LLaMA model
llama_model_path = os.getenv("RAG_MODEL_PATH") or "/data/LLMs/gguf/Llama-3.2-3B-Instruct-Q4_K_M.gguf"
llama = Llama(model_path=llama_model_path, n_ctx=0)

MAX_PORT_NUMBER = 65_535

def retrieve_documents(query, collection_name, top_k=1):
    collection = chroma_client.get_collection(name=collection_name, embedding_function=embedding_function)
    results = collection.query(query_texts=[query], n_results=top_k)
    documents = results["documents"]
    return [doc for sublist in documents for doc in sublist]

def generate_response(query, collection_name):
    documents = retrieve_documents(query, collection_name)
    context = "\n".join(documents)

    prompt = f"""
### CONTEXT:
{context}

### QUERY:
{query}

Answer the user's QUERY using the CONTEXT above.
If the CONTEXT doesn’t contain enough information, reply with: "I do not know."

### Answer:
"""

    full_response = ""
    for output in llama(prompt, max_tokens=4096, stream=True):
        token_text = output['choices'][0]['text']
        full_response += token_text
        yield "", [(query, full_response)], [(query, full_response)], gr.Textbox.update(value=context, visible=True)

    return "", [(query, full_response)], [(query, full_response)]

def main():
    with gr.Blocks(theme=IBMTheme()) as demo:
        gr.Markdown("# Chatbot about IBM RedBooks running on IBM POWER10")

        topic_choices = set()
        with open("database_setup.txt", "r") as f:
            for line in f:
                if ":" in line:
                    topic_choices.add(line.split(":")[0].strip())

        chatbot = gr.Chatbot(label="Chatbot", elem_id="chatbot", height=400).style(container=True)
        context_box = gr.Textbox(lines=8, interactive=False, visible=False, label="Source from Documents in Vector DB")
        query_input = gr.Textbox(show_label=False, placeholder="Enter your query here...", container=False)
        topic_dropdown = gr.Dropdown(label="Which POWER Topic?", choices=sorted(topic_choices))
        submit_button = gr.Button("Submit")

        submit_button.click(
            fn=generate_response,
            inputs=[query_input, topic_dropdown],
            outputs=[query_input, chatbot, chatbot, context_box]
        )

    port = int(os.getenv("RAG_PORT", "7680"))
    if not (1 <= port <= MAX_PORT_NUMBER):
        raise ValueError(f"PORT {port} is outside valid range 1-{MAX_PORT_NUMBER}")
    
    demo.launch(server_name="0.0.0.0", server_port=port, enable_queue=True)

if __name__ == "__main__":
    main()

