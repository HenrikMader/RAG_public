import gradio as gr
import chromadb
import os
from chromadb.utils import embedding_functions
from sentence_transformers import CrossEncoder
from openai import OpenAI

# Initialize OpenAI client
openai_client = OpenAI(
    base_url="http://localhost:11434/v1",  # Ollama API endpoint
    api_key="ollama"  # dummy, required by client but not used
)


# Embedding + reranker setup
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-mpnet-base-v2"
)
reranker = CrossEncoder("jinaai/jina-reranker-v2-base-multilingual", trust_remote_code=True)

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./db")

MAX_PORT_NUMBER = 65_535

# Retrieve relevant docs from ChromaDB
def retrieve_documents(query, collection_name, top_k=20):
    collection = chroma_client.get_collection(
        name=collection_name, embedding_function=sentence_transformer_ef
    )
    results = collection.query(query_texts=[query], n_results=top_k)
    return results["documents"][0]

# Rerank docs
def rerank_documents(query, documents, top_k=5):
    pairs = [(query, doc) for doc in documents]
    scores = reranker.predict(pairs)
    scored_docs = list(zip(documents, scores))
    ranked = sorted(scored_docs, key=lambda x: x[1], reverse=True)
    return [doc for doc, score in ranked[:top_k]]

def generate_response(query, collection_name, chat_history):
    documents = retrieve_documents(query, collection_name, top_k=10)
    top_documents = rerank_documents(query, documents, top_k=2)

    context = "\n".join(
        f"--------- Chunk {i+1}:\n{doc}\n" for i, doc in enumerate(top_documents)
    )

    system_prompt = f"""
    You are a Retrieval-Augmented Generation (RAG) assistant. Follow these instructions:

    1. Use ONLY the information provided in the DOCUMENTS below.
    2. Ground your answer in those documents
    3. Be concise and factual.

    ### DOCUMENTS:
    {context}
    """

    ## 

    stream = openai_client.chat.completions.create(
        model="granite3.3:2b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        stream=True,
        max_tokens=512,
    )

    cmData = ""
    for chunk in stream:  # ✅ iterate over ChatCompletionChunk objects
        if chunk.choices and chunk.choices[0].delta:  # check delta exists
            token = chunk.choices[0].delta.content or ""
            cmData += token

            if token:  # only yield when real text arrives
                partial_history = [(query, cmData)]

                if len(chat_history) >= 1:
                    chat_history.pop(0)

                helper = chat_history + [
                    ("User Input: " + partial_history[0][0],
                     "Answer from Chatbot: " + partial_history[0][1])
                ]

                yield "", partial_history, helper, gr.Textbox.update(
                    value=context, visible=True
                )

    return "", chat_history + [(query, cmData)], chat_history + [(query, cmData)]




# Build Gradio UI
def main():
    with gr.Blocks() as demo:
        gr.Markdown("# Chatbot about IBM RedBooks running on IBM POWER10")

        chat_history = gr.State([])

        collections = chroma_client.list_collections()
        choices = {col.name for col in collections}

        with gr.Row():
            chatbot = gr.Chatbot(label="Chatbot", elem_id="chatbot", height=400).style(container=True)

        with gr.Row():
            retreival_vector_db = gr.Textbox(
                lines=8, interactive=False, visible=False,
                label="Source from Documents in Vector DB"
            )

        with gr.Row():
            query_input = gr.Textbox(
                show_label=False, placeholder="Enter your query here...", container=False
            )
            file_selector = gr.Dropdown(label="Which POWER Topic?", choices=choices)

        with gr.Row():
            submit_button = gr.Button("Submit")

        submit_button.click(
            fn=generate_response,
            inputs=[query_input, file_selector, chat_history],
            outputs=[query_input, chatbot, chat_history, retreival_vector_db]
        )

    server_port = int(os.getenv("RAG_PORT", "7680"))
    if not (1 <= server_port <= MAX_PORT_NUMBER):
        raise ValueError(f"PORT {server_port} outside of valid port Range 1-{MAX_PORT_NUMBER}!")

    demo.queue()
    demo.launch(server_name="0.0.0.0", server_port=server_port)

if __name__ == "__main__":
    main()
