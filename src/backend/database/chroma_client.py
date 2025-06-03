# chroma run
from typing import List
import chromadb

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

class ChromaClient:
    def __init__(self, db_info, collection_name, remote=False):
        if not remote:
            self.client = chromadb.PersistentClient(path=db_info['db_dir'])
        else:
            self.client = chromadb.HttpClient(host = db_info['host'], port = db_info['port'])
        self.collection = self.client.get_or_create_collection(collection_name)
        
    def add_document(self, document: str, metadatas: List["MetadataDict"]):

        for metadata in metadatas:
            self.collection.upsert(
                documents=[metadata["text_chunk"]],
                metadatas=[{"source_title": metadata["source_title"], 
                            "source_author": metadata["source_author"]}],
                ids=[metadata["id"]],
                embeddings=[metadata["embedding"]]
            )

        print(f"Document with name {document} added to ChromaDB.")
        return document
    
    def get_document_by_id(self, document_id: str):
        results = self.collection.get(
            ids=[document_id],
            include=["documents", "metadatas", "embeddings"]
        )
        return results
        
    def find_similar_documents(self, embedding: list, n_results: int = 5):
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results,
            include=["documents", "metadatas", "embeddings"]
        )
        return results

    def find_and_print_similar_documents(self, embedding: list, n_results: int = 5):
        results = self.find_similar_documents(embedding, n_results)

        for i, doc in enumerate(results['documents'][0]):
            metadata = results['metadatas'][0][i]
            print(f"\nID: {results['ids'][0][i]}")
            print(f"  Document: {doc}")
            print(f"  Source Title: {metadata['source_title']}")
            print(f"  Source Author: {metadata['source_author']}")
            print(f"  Text: {metadata['text_chunk']}")
            print(f"  Embedding: {results['embeddings'][0][i]}")