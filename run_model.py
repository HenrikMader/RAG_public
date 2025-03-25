import gradio as gr
import chromadb
from llama_cpp import Llama
import os
from chromadb.utils import embedding_functions
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import time
import re
from theme import IBMTheme



# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./db")

# Initialize LLaMA model with llama-cpp-python (local model)
llama_model_path = os.getenv("RAG_MODEL_PATH") or "ibm-granite_granite-3.2-8b-instruct-Q4_K_M.gguf"
llama = Llama(model_path=llama_model_path, n_ctx=0)

#model = SentenceTransformer('all-mpnet-base-v2')
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

MAX_PORT_NUMBER = 65_535

# Function to retrieve relevant documents from ChromaDB
def retrieve_documents(query, collection_name, top_k=1):
 
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



    # Use context if needed
    use_context = True

    print("Chat history")
    print(chat_history)

    if use_context:
        documents = retrieve_documents(query, collection_name)
        print(documents)
        flat_documents = [item for sublist in documents for item in sublist]
        context = "\n".join(flat_documents)

        input_text = input_text = f"""
### CONTEXT:
{context}

### CHAT HISTORY:
{chat_history}

### QUERY:
{query}


Answer the users QUERY using the DOCUMENT or CHAT HISTORY text above.
Keep your answer ground in the facts of the DOCUMENT.
If the DOCUMENT doesn’t contain the facts to answer the QUERY, then state "I do not know".

### Answer:
"""

        print("input text")
        print(input_text)
        
    else:
        input_text = f"Query: {query}\nAnswer: "

    # Prepare a string to accumulate the model’s streamed tokens
    cmData = ""
    
    stopThinking = False
    for output in llama(input_text, max_tokens=4096, stream=True):
        token_text = output['choices'][0]['text']
        print(token_text)
        #if (token_text == "</think>"):
            #stopThinking = True
            #print("stop thinking true")

        #if (stopThinking == True and token_text != "</think>"):
        cmData += token_text
            
        # Each time we get new tokens, we yield an updated chat history
        partial_history = [(query, cmData)]
        
        #partial_history[0] = "User Question:" + partial_history[0] 
        
        #print("partial_history")
        #print(partial_history)
        
        #print("partial history here")
        #print(partial_history[0][0])
        
        if (len(chat_history) >= 3):
            chat_history.pop(0)

        helper = chat_history + [(("User Input: " + partial_history[0][0]), ("Answer from Chatbot: " + partial_history[0][1]))]
        
        

        #print("helper")
        #print(helper)
        
            #print(partial_history)

        # Yield both the updated input and chat history
        yield "", partial_history, helper, gr.Textbox.update(value=context, visible=True)  # Return chat history twice (for chatbot & state)
    
    print("final answer")
    print(chat_history + [(query, cmData)])
    # **Ensure final chat history is properly returned**
    return "", chat_history + [(query, cmData)], chat_history + [(query, cmData)]

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

    with gr.Blocks(theme=IBMTheme()) as demo:
        gr.Markdown("# Chatbot about IBM RedBooks running on IBM POWER10")

        # A hidden state to store the chat hi:wq story (list of (user, bot) tuples).
        chat_history = gr.State([])

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
