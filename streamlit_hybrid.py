import streamlit as st
import chromadb
import os
from chromadb.utils import embedding_functions
from sentence_transformers import CrossEncoder
from openai import OpenAI
import time
from datetime import datetime

# Configuration for different deployment modes
DEPLOYMENT_CONFIGS = {
    "On-Premise (Ollama)": {
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
        "model": "gemma4:e2b",
        "timeout": 120,
        "description": "Local Ollama instance - Free, Private, No internet required"
    },
    "Cloud (OpenAI)": {
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
        "model": "gpt-4",
        "timeout": 60,
        "description": "OpenAI GPT-4 - Highest quality, Requires API key"
    },
    "Cloud (Custom Endpoint)": {
        "base_url": "https://your-custom-endpoint.com/v1",  # Configure your endpoint here
        "api_key_env": "CUSTOM_API_KEY",
        "model": "your-model-name",
        "timeout": 60,
        "description": "Custom cloud endpoint - Configure in code"
    }
}

MAX_PORT_NUMBER = 65_535
MAX_RETRIES = 3

# Initialize OpenAI client based on deployment mode
@st.cache_resource
def get_openai_client(deployment_mode):
    """Get OpenAI client configured for selected deployment mode"""
    config = DEPLOYMENT_CONFIGS[deployment_mode]
    
    # Get API key
    if "api_key_env" in config:
        api_key = os.getenv(config["api_key_env"])
        if not api_key:
            st.error(f"❌ {config['api_key_env']} environment variable not set!")
            st.info(f"Set it with: export {config['api_key_env']}='your-key'")
            return None
    else:
        api_key = config["api_key"]
    
    return OpenAI(
        base_url=config["base_url"],
        api_key=api_key
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

def generate_response(query, collection_name, chat_history, deployment_mode):
    """Generate response using selected deployment mode"""
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

    print(system_prompt)
    openai_client = get_openai_client(deployment_mode)
    if not openai_client:
        raise Exception("Failed to initialize OpenAI client")
    
    config = DEPLOYMENT_CONFIGS[deployment_mode]
    
    # Build messages
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": query}]
    
    # Attempt with retry logic
    for attempt in range(MAX_RETRIES):
        try:
            stream = openai_client.chat.completions.create(
                model=config["model"],
                messages=messages,
                stream=True,
                max_tokens=512,
                timeout=config["timeout"],
            )
            return stream, context
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                wait_time = 2 ** attempt
                time.sleep(wait_time)
                continue
            else:
                raise Exception(f"Failed after {MAX_RETRIES} attempts: {str(e)}")

def save_conversation_to_file(messages, collection_name, deployment_mode):
    """Save conversation to a text file with timestamp"""
    if not messages:
        return None, "No conversation to save!"
    
    os.makedirs("conversations", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"conversation_{timestamp}.txt"
    filepath = os.path.join("conversations", filename)
    
    conversation_text = f"""=====================================
IBM RedBooks Conversation Log
=====================================
Collection: {collection_name}
Deployment Mode: {deployment_mode}
Date: {datetime.now().strftime("%Y-%m-%d")}
Total Messages: {len(messages) / 2}
=====================================

"""
    
    for i, msg in enumerate(messages, 1):
        role = "USER" if msg["role"] == "user" else "ASSISTANT"
        conversation_text += f"{role}:\n{msg['content']}\n\n"
        conversation_text += "---\n\n"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(conversation_text)
        return conversation_text, f"Conversation saved successfully to {filename}"
    except Exception as e:
        return None, f"Error saving file: {str(e)}"

def generate_summary(messages, deployment_mode):
    """Generate a summary of the conversation using the LLM"""
    if not messages:
        return "No conversation to summarize."
    
    conversation_text = ""
    for msg in messages:
        role = "USER" if msg["role"] == "user" else "ASSISTANT"
        conversation_text += f"{role}: {msg['content']}\n\n"
    
    summary_prompt = f"""This is a conversation from a user with a chatbot during an on-duty call. Please summarize this conversation so it can be presented to team members of my company.

    Focus on:
    - Key questions asked
    - Main topics discussed
    - Important technical information provided
    - Any action items or decisions (if applicable)

CONVERSATION:
{conversation_text}

Provide a concise, professional summary suitable for team review."""
    
    try:
        openai_client = get_openai_client(deployment_mode)
        if not openai_client:
            return "Error: Could not initialize client for summary generation"
        
        config = DEPLOYMENT_CONFIGS[deployment_mode]
        response = openai_client.chat.completions.create(
            model=config["model"],
            messages=[{"role": "user", "content": summary_prompt}],
            stream=False,
            max_tokens=1024,
            timeout=config["timeout"],
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
        :root {
            --ibm-blue: #0f62fe;
            --ibm-blue-dark: #0043ce;
            --ibm-blue-light: #4589ff;
            --ibm-gray: #161616;
            --ibm-gray-light: #f4f4f4;
        }
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        .ibm-header {
            background: linear-gradient(135deg, #0f62fe 0%, #0043ce 100%);
            padding: 2rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .deployment-badge {
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            font-weight: 600;
            margin-top: 0.5rem;
        }
        
        .badge-onpremise {
            background-color: #24a148;
            color: white;
        }
        
        .badge-cloud {
            background-color: #0f62fe;
            color: white;
        }
        </style>

        <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
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
    
    if "deployment_mode" not in st.session_state:
        st.session_state.deployment_mode = "On-Premise (Ollama)"

    # Get available collections
    chroma_client = get_chroma_client()
    collections = chroma_client.list_collections()
    choices = [col.name for col in collections]

    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Deployment mode selector
        st.subheader("🌐 Deployment Mode")
        deployment_mode = st.selectbox(
            "Select Deployment",
            list(DEPLOYMENT_CONFIGS.keys()),
            key="deployment_selector",
            help="Choose between on-premise (Ollama) or cloud deployment"
        )
        
        # Store in session state
        st.session_state.deployment_mode = deployment_mode
        
        # Display deployment info
        config = DEPLOYMENT_CONFIGS[deployment_mode]
        st.info(f"ℹ️ {config['description']}")
        
        # Show model being used
        st.caption(f"Model: `{config['model']}`")
        
        st.markdown("---")
        
        # Collection selector
        st.subheader("📚 Knowledge Base")
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
                    selected_collection,
                    deployment_mode
                )
                if conversation_text:
                    st.success(message)
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
                    st.session_state.summary = generate_summary(
                        st.session_state.messages,
                        deployment_mode
                    )
                    st.session_state.show_summary = True
                st.success("Summary generated!")
                st.rerun()
        
        st.markdown("---")
        
        # System info
        st.caption("💡 **Tips:**")
        if "On-Premise" in deployment_mode:
            st.caption("• Ollama must be running locally")
            st.caption("• Free and private")
            st.caption("• No internet required")
        else:
            st.caption("• Requires API key")
            st.caption("• Higher quality responses")
            st.caption("• Internet connection needed")

    # IBM Header with deployment badge
    badge_class = "badge-onpremise" if "On-Premise" in deployment_mode else "badge-cloud"
    st.markdown(f"""
        <div class="ibm-header">
            <h1>🔵 IBM RedBooks AI Assistant</h1>
            <p>Powered by IBM POWER10 | Granite 4</p>
            <span class="deployment-badge {badge_class}">{deployment_mode}</span>
        </div>
        """, unsafe_allow_html=True)

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

        # Generate response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                stream, context = generate_response(
                    prompt, 
                    selected_collection, 
                    st.session_state.chat_history,
                    deployment_mode
                )
                
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta:
                        token = chunk.choices[0].delta.content or ""
                        full_response += token
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # Add to chat history
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                st.session_state.chat_history.append({"role": "assistant", "content": full_response})
                
                # Store assistant response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response
                })
                
                # Store context for display
                st.session_state.last_context = context
                st.session_state.show_context = True
                
            except Exception as e:
                st.error(f"❌ Error generating response: {str(e)}")
                if "On-Premise" in deployment_mode:
                    st.info("💡 Make sure Ollama is running: `ollama serve`")
                else:
                    st.info("💡 Check your API key and internet connection")

    # Display source context if available
    if st.session_state.show_context and "last_context" in st.session_state:
        with st.expander("📚 Source Documents from Vector Database", expanded=False):
            st.text(st.session_state.last_context)

if __name__ == "__main__":
    server_port = int(os.getenv("RAG_PORT", "7680"))
    if not (1 <= server_port <= MAX_PORT_NUMBER):
        raise ValueError(f"PORT {server_port} outside of valid port Range 1-{MAX_PORT_NUMBER}!")
    
    main()

# Made with Bob
