import chromadb
import os
from chromadb.utils import embedding_functions
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import time
from sentence_transformers import CrossEncoder
from run_model import rerank_documents

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")




# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./db")

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
    retrieved_documents = results["documents"]
    return retrieved_documents


query = "How many cores does the Power11 system has?"
collection_name = "POWER11"
documents = retrieve_documents(query, collection_name)
print(documents)
print("After reranking")
top_documents = rerank_documents(query, documents[0], top_k=5)
print(top_documents)

