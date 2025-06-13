import sys
from enum import auto
from enum import Enum
from pathlib import Path
from typing import Optional
import chromadb
from chromadb.utils import embedding_functions
from chromadb import Collection
from transformers import AutoTokenizer, AutoModel
import os
import re
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
import time

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on, strip_headers=False)
recursive_splitter = RecursiveCharacterTextSplitter(chunk_size=500)


class CollectionStatus(Enum):
    COLLECTION_CREATED = auto()
    COLLECTION_EXISTS = auto()


def ensure_collection(client: chromadb.ClientAPI, collection_name: str) -> tuple[str, Optional[Collection]]:
    try:
        # Check if the collection already exists
        collection = client.get_collection(name=collection_name, embedding_function=sentence_transformer_ef)
        print(f"Collection '{collection_name}' already exists.")
        return "COLLECTION_EXISTS", collection
    except Exception:
        # If it doesn't exist, create a new collection
        try:
            collection = client.create_collection(name=collection_name, embedding_function=sentence_transformer_ef)
            print(f"Collection '{collection_name}' created successfully.")
            return "COLLECTION_CREATED", collection
        except Exception as e:
            print(f"Failed to create collection '{collection_name}': {e}")
            return "COLLECTION_CREATION_FAILED", None


def clean_text(raw_text: str) -> str:
    # Clean up the text to remove extra spaces and line breaks
    cleaned_text = raw_text.replace("\n", " ")
    cleaned_text = re.sub(r"\s+", " ", raw_text)
    return cleaned_text

## This is Character Splitting. Not optimal
#def get_chunks(text: str, max_words: int = 150) -> list[tuple[str, int]]:
#    words = clean_text(text).split(" ")
#    chunks = []
    # Split the text into chunks of max_words length
#    for i in range(0, len(words), max_words):
#        chunk = words[i:i + max_words]
#        chunk_text = " ".join(chunk).strip()
#        chunks.append((chunk_text, i // max_words))
#    return chunks




def insert_document(document_path: Path, collection: Collection) -> None:
    """
    Reads a markdown file, splits it into chunks, generates embeddings,
    and inserts the chunks into a ChromaDB collection.
    """
    # Read the markdown file content
    with open(document_path, 'r') as file:
        markdown_content = file.read()
    
    #markdown_content = clean_text(markdown_content)

    text = splitter.split_text(markdown_content)    
    
    document_name = document_path.stem.replace(" ", "-").replace("_", "-")

    # Get chunks of text from the markdown content
    #chunks = get_chunks(markdown_content)
    document_chunks = []
    document_ids = []

    #print("Whole text")
    #print(text)
    for chunk_index, chunk in enumerate(text):
        
        #sub_chunks = recursive_splitter.split_text(chunk.page_content)

        #for sub_index, sub_chunk in enumerate(sub_chunks):
        document_ids.append(f"{document_name}_chunk{chunk_index}")
        document_chunks.append(chunk.page_content)

    
    collection.add(
                documents=document_chunks,
                ids=document_ids
            )
    

    '''
    print("Adding chunks to collection:")
    #print(document_chunks)

    # Add documents with embeddings to the ChromaDB collection
    batch_size = len(document_chunks) // 100  # Calculate 10% of chunks
    if batch_size == 0:  # Handle small input where 10% is less than 1
        batch_size = 1

    # Iterate through document_chunks in batches
    for i in range(0, len(document_chunks), batch_size):
        batch_chunks = document_chunks[i:i + batch_size]
        batch_ids = document_ids[i:i + batch_size]
        print(batch_ids)

        print(f"Before batch {i}, Memory Usage: {psutil.virtual_memory().percent}%")
        try:
            collection.add(
                documents=batch_chunks,
                ids=batch_ids
            )
        except Exception as e:
            print(f"Error occurred: {e}")
        print(f"After batch {i}, Memory Usage: {psutil.virtual_memory().percent}%")
'''


## Folder_path = path to e config files
def load_files_into_chroma(folder_path, client: chromadb.ClientAPI, collection_name):
    # Iterate over files in the folder

    collection_status, collection = ensure_collection(client, collection_name)


    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Only process text files (or adapt as needed for other file types)
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            # Open and read the content of each file
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            


            # Add the file content to the Chroma collection as a new chunk
            collection.add(
                documents=[file_content],
                metadatas=[{"filename": filename}],
                ids=[filename]
            )
            print(f"Added {filename} to Chroma database.")



def main() -> None:
    base_directory = Path(os.getcwd())
    db_directory = Path("./db")
    files_directory = Path("./db_files_md")  # Folder containing markdown files

    if not db_directory.exists():
        db_directory.mkdir()

    if not files_directory.exists():
        print("DB files were not copied! Abort.")
        sys.exit(1)

    chroma_client = chromadb.PersistentClient(path=str(db_directory))

    ## Inserting e config files firt

    #load_files_into_chroma("./db_config", chroma_client, "e_config_files")

    file = open("database_setup.txt")
    for i in file:
        print(i)
        x = i.split(":", 1)
        collection_name = str(x[0]).strip()
        file_name = str(x[1]).strip()
        print("Adding")
        print(file_name)
        print("to")
        print(collection_name)
        
        print(type(collection_name))
        # Ensure the collection exists or create it
        collection_status, collection = ensure_collection(chroma_client, str(collection_name))

        if collection_status == CollectionStatus.COLLECTION_EXISTS:
            print(f"Collection '{collection_name}' already exists. Skipping file insertion.")
        else:
            print(f"Creating collection '{collection_name}' and inserting documents.")
            
            # Process the file
            #document_path = Path(".") / files_directory / Path(file_name)
            document_path = files_directory / file_name
            print(document_path)
            if document_path.exists():
                insert_document(document_path, collection)
                print(f"Inserted {file_name} into {collection_name}")
            else:
        from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.pipeline.vlm_pipeline import VlmPipeline
from docling.datamodel.pipeline_options import (
    VlmPipelineOptions,
)
from docling.datamodel import vlm_model_specs

pipeline_options = VlmPipelineOptions(
    vlm_options=vlm_model_specs.SMOLDOCLING_MLX,  # <-- change the model here
)

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_cls=VlmPipeline,
            pipeline_options=pipeline_options,
        ),
    }
)

doc = converter.convert(source="FILE").document        print(f"File {file_name} not found!")
            
            # Delay between operations

    # Final collection with all the markdown files in the directory
    #final_collection_name = "final_collection_all_files"
    #collection_status, collection = ensure_collection(chroma_client, final_collection_name)

    #if collection_status == CollectionStatus.COLLECTION_EXISTS:
    #    print(f"Collection '{final_collection_name}' already exists. Skipping file insertion.")
    #else:
    #    print(f"Creating collection '{final_collection_name}' and inserting all documents.")
    #    for document_path in files_directory.glob("*.md"):  # Insert all .md files
    #        insert_document(document_path, collection)
    #        print(f"Inserted {document_path.name} into {final_collection_name}")
    #        time.sleep(5)

    print("Setup completed.")

    # Example query for testing
    result = collection.query(
        query_texts=["What is IBM POWER"],
        n_results=5,
        include=["documents"]
    )
    print(result)


if __name__ == "__main__":
    main()
                                                       
