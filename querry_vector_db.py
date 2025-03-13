import chromadb
from chromadb import Client
from sentence_transformers import SentenceTransformer
from pathlib import Path
import os
 
 
base_directory = Path(os.getcwd()) 
 
database = base_directory / "db" 
# Initialize Chroma client and collection
chroma_client = chromadb.PersistentClient(path="./db")   # Change path accordingly
collection = chroma_client.get_collection(name="collection_group_1") 
 
results = collection.query( 
    query_texts=["What is IBM POWER?"], 
    n_results=5, 
    include=["documents"] 
) 
 
print(results) 
 
