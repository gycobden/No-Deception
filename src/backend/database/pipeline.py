from .chunker import chunk_file
from .embedder import embed_chunk
from .chroma_client import MetadataDict, add_document

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

    # Create a MetadataDict objects from file_name to insert
    # into the database
    data = {
        "ids": ids,
        "chunks": chunks,
        "embeddings": embeddings,
        "metadata": metadata
    }
    
    for chunk_id, chunk, embedding in enumerate(zip(ids, chunks, embeddings)):
        print(f"Adding id {chunk_id} to database with title {metadata['title']} and author {metadata['author']}\n")
        metadata_dict = MetadataDict(
            id=f"{chunk_id}",
            embedding=embedding,
            text_chunk=chunk,
            source_title=metadata["title"], 
            source_author=metadata["author"]
        )
        add_document(metadata["title"], metadata_dict)
        # Add the metadata to the data dictionary
        data["chunks"][chunk_id] = {
            "id": chunk_id,
            "metadata": {
                "title": metadata["title"],
                "author": metadata["author"],
            },
            "chunk": chunk,
            "embedding": embedding
        }

    return data

if __name__ == "__main__":
    process_file("../vaccine.pdf")