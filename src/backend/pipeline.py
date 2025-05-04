from chunker import chunk_file
from embedder import embed_chunk

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

def upload_file(file_name):
    ids, chunks, metadata = chunk_file(file_name)
    embeddings = embed_chunk(chunks)

    print(ids, chunks, metadata["title"], metadata["author"], embeddings)

if __name__ == "__main__":
    upload_file("vaccine.pdf")