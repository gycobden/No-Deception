# chroma run

import chromadb
from chromadb import Client, Collection
import pprint # for pretty printing

chroma_client = chromadb.PersistentClient(path="/Users/evanz/Documents/coding/No-Deception/src/backend/database") # save and load db from local machine
chroma_client = chromadb.HttpClient(host="localhost", port="8000") # connect to chroma server

collection = chroma_client.get_or_create_collection(name="vaccine_documents")

# MetadataDict class is used to hold metadata for each document and converts them in the
# correct format to be added to the ChromaDB collection
class MetadataDict:
    def __init__(self, id: str, embedding: list, text_chunk: str, source_title: str, source_author: str):
        self.id = id
        self.embedding = embedding
        self.text_chunk = text_chunk
        self.source_title = source_title
        self.source_author = source_author

    def to_dict(self):
        return {
            "id": self.id,
            "embedding": self.embedding,
            "text_chunk": self.text_chunk,
            "source_title": self.source_title,
            "source_author": self.source_author,
        }
    
def add_document(document: str, metadata: MetadataDict):
    collection.upsert(
        documents=[document],
        metadatas=[{"id": metadata["id"], "text_chunk": metadata["text_chunk"], "source_title": metadata["source_title"], 
                    "source_author": metadata["source_author"]}],
        ids=[metadata["id"]],
        embeddings=[metadata["embedding"]]
    )
    print(f"Document with ID {metadata["id"]} added to ChromaDB.")
    return metadata["id"]

def get_document_by_id(document_id: str):
    results = collection.get(
        ids=[document_id],
        include=["documents", "metadatas", "embeddings"]
    )
    return results
    
def find_similar_documents(embedding: list, n_results: int = 5):
    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results,
        include=["documents", "metadatas", "embeddings"]
    )
    return results

def find_and_print_similar_documents(embedding: list, n_results: int = 5):
    results = find_similar_documents(embedding, n_results)

    for i, doc in enumerate(results['documents'][0]):
        metadata = results['metadatas'][0][i]
        print(f"\nID: {metadata['id']}")
        print(f"  Document: {doc}")
        print(f"  Source Title: {metadata['source_title']}")
        print(f"  Source Author: {metadata['source_author']}")
        print(f"  Text: {metadata['text_chunk']}")
        
        print(f"  Embedding: {results['embeddings'][0][i]}")