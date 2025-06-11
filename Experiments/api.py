from flask import Flask, request, jsonify, stream_with_context, Response
from flask_cors import CORS
from llama_cpp import Llama
import os
from chromadb.utils import embedding_functions
import chromadb
import json
from threading import Lock
import time

app = Flask(__name__)
CORS(app)


def retrieve_documents(query, collection_name, top_k=1):
 
    collection = chroma_client.get_collection(name=collection_name, embedding_function=sentence_transformer_ef)
    
    #query_embedding = model.encode([query])[0]

    # Perform similarity search with ChromaDB
    results = collection.query(query_texts=[query], n_results=top_k)
    
    # Extract the documents
    retrieved_documents = results["documents"]
    return retrieved_documents


# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./db")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

# Initialize LLaMA model
llama_model_path = os.getenv("RAG_MODEL_PATH") or "granite-3.3-2b-instruct-Q4_K_M.gguf"
llama = Llama(model_path=llama_model_path, n_ctx=0)

# Lock for model access
model_lock = Lock()

@app.route("/v1/models", methods=["GET"])
def list_models():
    """List available models."""
    return jsonify({
        "data": [{
            "id": "granite-3.3-2b-instruct",
            "object": "model",
            "owned_by": "ibm",
            "permissions": []
        }],
        "object": "list"
    })

@app.route("/v1/chat/completions", methods=["POST"])
def chat_completions():
    """Handle chat completion requests."""
    data = request.get_json()
    
    # Validate request
    if not data or "messages" not in data:
        return jsonify({"error": "messages field is required"}), 400
    
    messages = data["messages"]
    model = data.get("model", "granite-3.3-2b-instruct")
    stream = data.get("stream", False)
    temperature = data.get("temperature", 0.7)
    max_tokens = data.get("max_tokens", 4096)
    
    # Extract last message as query
    query = messages[-1].get("content", "")
    collection_name = "POWER10"
    
    # Get chat history
    chat_history = []
    for msg in messages:
        if msg["role"] == "user":
            chat_history.append((msg["content"], ""))
        elif msg["role"] == "assistant":
            chat_history[-1] = (chat_history[-1][0], msg["content"])
    
    def generate_stream():
        with model_lock:
            # Use context if needed
            documents = retrieve_documents(query, collection_name)
            flat_documents = [item for sublist in documents for item in sublist]
            context = "\n".join(flat_documents)
            
            input_text = f"""
### CONTEXT:
{context}

### CHAT HISTORY:
{chat_history}

### QUERY:
{query}

Answer the users QUERY using the DOCUMENT or CHAT HISTORY text above.
Keep your answer ground in the facts of the DOCUMENT.
If the DOCUMENT doesn't contain the facts to answer the QUERY, then state "I do not know".

### Answer:
"""
            
            cmData = ""
            for output in llama(input_text, max_tokens=max_tokens, temperature=temperature, stream=True):
                token_text = output['choices'][0]['text']
                cmData += token_text
                
                # Stream response
                response_chunk = {
                    "id": "chatcmpl-" + os.urandom(10).hex(),
                    "object": "chat.completion.chunk",
                    "created": int(time.time()),
                    "model": model,
                    "choices": [{
                        "index": 0,
                        "delta": {"content": token_text},
                        "finish_reason": None
                    }]
                }
                yield 'data: ' + json.dumps(response_chunk) + '\n\n'
            
            # Final response
            final_chunk = {
                "id": "chatcmpl-" + os.urandom(10).hex(),
                "object": "chat.completion.chunk",
                "created": int(time.time()),
                "model": model,
                "choices": [{
                    "index": 0,
                    "delta": {},
                    "finish_reason": "stop"
                }]
            }
            yield 'data: ' + json.dumps(final_chunk) + '\n\n'
            yield "data: [DONE]\n\n"
    
    if stream:
        return Response(
            stream_with_context(generate_stream()),
            mimetype="text/event-stream"
        )
    
    # Non-streaming response
    with model_lock:
        documents = retrieve_documents(query, collection_name)
        flat_documents = [item for sublist in documents for item in sublist]
        context = "\n".join(flat_documents)
        
        input_text = f"""
### CONTEXT:
{context}

### CHAT HISTORY:
{chat_history}

### QUERY:
{query}

Answer the users QUERY using the DOCUMENT or CHAT HISTORY text above.
Keep your answer ground in the facts of the DOCUMENT.
If the DOCUMENT doesn't contain the facts to answer the QUERY, then state "I do not know".

### Answer:
"""
        
        output = llama(input_text, max_tokens=max_tokens, temperature=temperature)
        response = output['choices'][0]['text']
        
        return jsonify({
            "id": "chatcmpl-" + os.urandom(10).hex(),
            "object": "chat.completion",
            "created": int(time.time()),
            "model": model,
            "choices": [{
                "index": 0,
                "message": {"content": response},
                "finish_reason": "stop"
            }],
            "usage": {
                "prompt_tokens": len(input_text.split()),
                "completion_tokens": len(response.split()),
                "total_tokens": len(input_text.split()) + len(response.split())
            }
        })

@app.route("/v1/embeddings", methods=["POST"])
def embeddings():
    """Handle embeddings requests."""
    data = request.get_json()
    if not data or "input" not in data:
        return jsonify({"error": "input field is required"}), 400
    
    input_text = data["input"]
    if isinstance(input_text, str):
        input_text = [input_text]
    
    embeddings = []
    for text in input_text:
        embedding = sentence_transformer_ef([text])[0]
        embeddings.append(embedding)
    
    return jsonify({
        "data": [{
            "embedding": embedding,
            "index": i,
            "object": "embedding"
        } for i, embedding in enumerate(embeddings)],
        "model": "sentence-transformer-all-mpnet-base-v2",
        "object": "list",
        "usage": {
            "prompt_tokens": sum(len(text.split()) for text in input_text),
            "total_tokens": sum(len(text.split()) for text in input_text)
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
