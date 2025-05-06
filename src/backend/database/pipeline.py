from .chunker import chunk_file
from .embedder import embed_chunk

"""
Reads in a PDF file, parse its text, extract the metadata, 
divides the parsed text in to text chunks, embeds those chunks 
with a embedding model, and upload the metadata, chunks, and embeddings
onto the vector database

Args:
    file_name: the PDF file to be processed.

Return:
    Void.
"""

def process_file(file_name):
    data = dict()

    ids, chunks, metadata = chunk_file(file_name)
    embeddings = embed_chunk(chunks)

    data["ids"] = ids
    data["chunks"] = chunks
    data["metadata"] = metadata
    data["embeddings"] = embeddings

    return data

if __name__ == "__main__":
    process_file("../vaccine.pdf")