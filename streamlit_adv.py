import streamlit as st
import chromadb
import os
from chromadb.utils import embedding_functions
from sentence_transformers import CrossEncoder
from openai import OpenAI
import time
from datetime import datetime

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

# Configuration for Ollama timeout and retries
OLLAMA_TIMEOUT = 120  # seconds
MAX_RETRIES = 3

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

def generate_response(query, collection_name, chat_history):
    documents = retrieve_documents(query, collection_name, top_k=10)
    top_documents = rerank_documents(query, documents, top_k=3)

    context = "\n".join(
        f"--------- Chunk {i+1}:\n{doc}\n" for i, doc in enumerate(top_documents)
    )

    system_prompt = f"""You are an IBM RedBooks AI Assistant specializing in IBM POWER systems.

RELEVANT DOCUMENTS:
{context}

INSTRUCTIONS:
1. Answer using ONLY the information from the documents above
2. If the answer is not in the documents, clearly state: "I don't find that information in the available documents"
3. Use the conversation history to understand context and follow-up questions
4. Provide detailed but focused answers (2-4 paragraphs for complex topics, 1-2 for simple questions)
5. When relevant, cite specific features, specifications, or capabilities from the documents
6. Stay technical and accurate - you're helping enterprise users with IBM POWER systems

Remember: Ground every statement in the provided documents."""

    openai_client = get_openai_client()
    
    # Build messages with history
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": query}]
    
    # Add previous chat history (excluding current query) - last 10 messages max
    
    # Add current query
    
    # Attempt with retry logic for concurrent access
    for attempt in range(MAX_RETRIES):
        try:
            stream = openai_client.chat.completions.create(
                model="granite4:tiny-h",
                messages=messages,
                stream=True,
                max_tokens=512,
                timeout=OLLAMA_TIMEOUT,
            )
            return stream, context
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
                continue
            else:
                raise Exception(f"Failed after {MAX_RETRIES} attempts: {str(e)}")

def save_conversation_to_file(messages, collection_name):
    """Save conversation to a text file with timestamp"""
    if not messages:
        return None, "No conversation to save!"
    
    # Create conversations directory if it doesn't exist
    os.makedirs("conversations", exist_ok=True)
    
    # Generate timestamp for filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"conversation_{timestamp}.txt"
    filepath = os.path.join("conversations", filename)
    
    # Format conversation
    conversation_text = f"""=====================================
IBM RedBooks Conversation Log
=====================================
Collection: {collection_name}
Date: {datetime.now().strftime("%Y-%m-%d")}
Total Messages: {len(messages) / 2}
=====================================

"""
    
    for i, msg in enumerate(messages, 1):
        role = "USER" if msg["role"] == "user" else "ASSISTANT"
        conversation_text += f"{role}:\n{msg['content']}\n\n"
        conversation_text += "---\n\n"
    
    # Save to file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(conversation_text)
        return conversation_text, f"Conversation saved successfully to {filename}"
    except Exception as e:
        return None, f"Error saving file: {str(e)}"

def generate_summary(messages):
    """Generate a summary of the conversation using the LLM"""
    if not messages:
        return "No conversation to summarize."
    
    # Build conversation string
    conversation_text = ""
    for msg in messages:
        role = "USER" if msg["role"] == "user" else "ASSISTANT"
        conversation_text += f"{role}: {msg['content']}\n\n"
    print(conversation_text)
    # Create summary prompt
    summary_prompt = f"""This is a conversation from a user with a chatbot during an on-duty call. Please summarize this conversation so it can be presented to team members of my company.

    Focus on:
    - Key questions asked
    - Main topics discussed
    - Important technical information provided
    - Any action items or decisions (if applicable)

CONVERSATION:
{conversation_text}

Provide a concise, professional summary suitable for team review."""
    
    # Call LLM without RAG
    try:
        openai_client = get_openai_client()
        response = openai_client.chat.completions.create(
            model="granite4:tiny-h",
            messages=[{"role": "user", "content": summary_prompt}],
            stream=False,
            max_tokens=1024,
            timeout=OLLAMA_TIMEOUT,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating summary: {str(e)}"

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
            <p>Powered by IBM POWER10 | Granite 4 |</p>
        </div>
        """, unsafe_allow_html=True)

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "show_context" not in st.session_state:
        st.session_state.show_context = False
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    if "summary" not in st.session_state:
        st.session_state.summary = None
    
    if "show_summary" not in st.session_state:
        st.session_state.show_summary = False

    # Get available collections
    chroma_client = get_chroma_client()
    collections = chroma_client.list_collections()
    choices = [col.name for col in collections]

    # Sidebar for collection selection
    with st.sidebar:
        st.header("Configuration")
        
        selected_collection = st.selectbox(
            "Select POWER Topic",
            choices,
            key="collection_selector",
            help="Choose which IBM RedBook collection to query"
        )
        
        st.markdown("---")
        
        # Save conversation button
        st.subheader("💾 Export")
        if st.button("Save Conversation", use_container_width=True):
            if len(st.session_state.messages) == 0:
                st.warning("No conversation to save yet!")
            else:
                conversation_text, message = save_conversation_to_file(
                    st.session_state.messages, 
                    selected_collection
                )
                if conversation_text:
                    st.success(message)
                    # Provide download button
                    timestamp = datetime.now().strftime("%Y-%m-%d")
                    st.download_button(
                        label="📥 Download File",
                        data=conversation_text,
                        file_name=f"conversation_{timestamp}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                else:
                    st.error(message)
        
        st.markdown("---")
        
        # Generate summary button
        st.subheader("📋 Summary")
        if st.button("Generate Summary", use_container_width=True):
            if len(st.session_state.messages) == 0:
                st.warning("No conversation to summarize yet!")
            else:
                with st.spinner("Generating summary..."):
                    st.session_state.summary = generate_summary(st.session_state.messages)
                    st.session_state.show_summary = True
                st.success("Summary generated!")
                st.rerun()

    # Display summary if generated
    if st.session_state.show_summary and st.session_state.summary:
        st.markdown(f"""
            <div class="summary-box">
                <h3>📋 Conversation Summary</h3>
            </div>
            """, unsafe_allow_html=True)
        st.markdown(st.session_state.summary)
        st.markdown("---")

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything about IBM POWER systems..."):
        if not selected_collection:
            st.error("⚠️ Please select a POWER Topic from the sidebar")
            return
        
        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Add user message to display messages
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate response (pass history WITHOUT current prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # Pass chat_history which does NOT include current prompt yet
                stream, context = generate_response(prompt, selected_collection, st.session_state.chat_history)
                
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta:
                        token = chunk.choices[0].delta.content or ""
                        full_response += token
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # NOW add both user prompt and assistant response to chat_history
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                st.session_state.chat_history.append({"role": "assistant", "content": full_response})
                
                # Store assistant response in display messages
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response
                })
                
                # Store context for display
                st.session_state.last_context = context
                st.session_state.show_context = True
                
            except Exception as e:
                st.error(f"❌ Error generating response: {str(e)}")

    # Display source context if available
    if st.session_state.show_context and "last_context" in st.session_state:
        with st.expander("📚 Source Documents from Vector Database", expanded=False):
            st.text(st.session_state.last_context)

if __name__ == "__main__":
    # Get port from environment variable
    server_port = int(os.getenv("RAG_PORT", "7680"))
    if not (1 <= server_port <= MAX_PORT_NUMBER):
        raise ValueError(f"PORT {server_port} outside of valid port Range 1-{MAX_PORT_NUMBER}!")
    
    # Note: Streamlit uses its own port configuration via command line
    # Run with: streamlit run app.py --server.port 7680 --server.address 0.0.0.0
    main()
