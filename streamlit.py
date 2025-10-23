import streamlit as st
import chromadb
import os
from chromadb.utils import embedding_functions
from sentence_transformers import CrossEncoder
from openai import OpenAI

# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    return OpenAI(
        base_url="http://localhost:11434/v1",  # Ollama API endpoint
        api_key="ollama"  # dummy, required by client but not used
    )

# Initialize embedding function and reranker
@st.cache_resource
def get_models():
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-mpnet-base-v2"
    )
    reranker = CrossEncoder("ibm-granite/granite-embedding-reranker-english-r2")
    return sentence_transformer_ef, reranker

# Initialize ChromaDB client
@st.cache_resource
def get_chroma_client():
    return chromadb.PersistentClient(path="./db")

MAX_PORT_NUMBER = 65_535

# Retrieve relevant docs from ChromaDB
def retrieve_documents(query, collection_name, top_k=20):
    chroma_client = get_chroma_client()
    sentence_transformer_ef, _ = get_models()
    collection = chroma_client.get_collection(
        name=collection_name, embedding_function=sentence_transformer_ef
    )
    results = collection.query(query_texts=[query], n_results=top_k)
    return results["documents"][0]

# Rerank docs
def rerank_documents(query, documents, top_k=5):
    _, reranker = get_models()
    pairs = [(query, doc) for doc in documents]
    scores = reranker.predict(pairs)
    scored_docs = list(zip(documents, scores))
    ranked = sorted(scored_docs, key=lambda x: x[1], reverse=True)
    return [doc for doc, score in ranked[:top_k]]

def generate_response(query, collection_name):
    documents = retrieve_documents(query, collection_name, top_k=20)
    top_documents = rerank_documents(query, documents, top_k=5)

    context = "\n".join(
        f"--------- Chunk {i+1}:\n{doc}\n" for i, doc in enumerate(top_documents)
    )

    system_prompt = f"""You are an AI Assistant for POWER systems.

    DOCUMENTS:
    {context}

    CRITICAL INSTRUCTIONS:
    1. Answer ONLY using the documents above
    2. If information is not in the documents, state: "I don't find that information in the available documents"
    3. Stay technical and accurate
    4. If a question is ambiguous, ask for clarification
    
    Remember: You are helping enterprise users - accuracy is paramount."""

    openai_client = get_openai_client()
    
    stream = openai_client.chat.completions.create(
        model="granite4:tiny-h",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        stream=True,
        max_tokens=512,
    )

    return stream, context

def main():
    
    st.set_page_config(
        page_title="IBM RedBooks Assistant",
        page_icon="🔵",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # IBM Custom CSS Styling
    st.markdown("""
        <style>
        /* IBM Color Palette */
        :root {
            --ibm-blue: #0f62fe;
            --ibm-blue-dark: #0043ce;
            --ibm-blue-light: #4589ff;
            --ibm-gray: #161616;
            --ibm-gray-light: #f4f4f4;
        }

        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Custom header */
        .ibm-header {
            background: linear-gradient(135deg, #0f62fe 0%, #0043ce 100%);
            padding: 2rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        </style>

        <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
        """, unsafe_allow_html=True)

    # IBM Header
    st.markdown("""
        <div class="ibm-header">
            <h1>🔵 IBM RedBooks AI Assistant</h1>
            <p>Powered by IBM POWER10 | Granite 4 </p>
        </div>
        """, unsafe_allow_html=True)

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "show_context" not in st.session_state:
        st.session_state.show_context = False

    # Get available collections
    chroma_client = get_chroma_client()
    collections = chroma_client.list_collections()
    choices = [col.name for col in collections]

    # Sidebar for collection selection
    with st.sidebar:
        st.header("Settings")
        selected_collection = st.selectbox(
            "Choose collection for Upload",
            choices,
            key="collection_selector"
        )

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Enter your query here..."):
        if not selected_collection:
            st.error("Please select a POWER Topic from the sidebar")
            return
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                stream, context = generate_response(prompt, selected_collection)
                
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta:
                        token = chunk.choices[0].delta.content or ""
                        full_response += token
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # Store assistant response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response
                })
                
                # Store context for display
                st.session_state.last_context = context
                st.session_state.show_context = True
                
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")

    # Display source context if available
    if st.session_state.show_context and "last_context" in st.session_state:
        with st.expander("📚 Source from Documents in Vector DB", expanded=False):
            st.text(st.session_state.last_context)

if __name__ == "__main__":
    # Get port from environment variable
    server_port = int(os.getenv("RAG_PORT", "7680"))
    if not (1 <= server_port <= MAX_PORT_NUMBER):
        raise ValueError(f"PORT {server_port} outside of valid port Range 1-{MAX_PORT_NUMBER}!")
    
    # Note: Streamlit uses its own port configuration via command line
    # Run with: streamlit run app.py --server.port 7680 --server.address 0.0.0.0
    main()
