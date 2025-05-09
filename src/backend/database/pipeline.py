from src.backend.database.chunker import chunk_file
from src.backend.database.embedder import embed_chunk
from src.backend.database.chroma_client import MetadataDict
from pathlib import Path

"""
Reads into a folder_path and get the path and name of all pdf files 
with in the folder.

Args:
    folder_path: str path to the folder

Returns:
    list of pdf objects, each containing the name of the pdf file and
    their full path
"""
def get_pdf_files(folder_path):
    folder = Path(folder_path)
    return list(folder.glob("*.pdf"))

"""
Reads in a PDF file, parse its text, extract the metadata, 
divides the parsed text in to text chunks, embeds those chunks 
with a embedding model, and upload the metadata, chunks, and embeddings
onto the vector database

Args:
    file_name: the PDF file to be processed.

Return:
    data: List of MetadataDict objects which contains data of each text_chunks
    file_name: The name of the document
"""
def process_file(file_name):
    data = dict()

    ids, chunks, metadata = chunk_file(file_name)
    embeddings = embed_chunk(chunks)

    data = []
    for i, embedding in enumerate(embeddings):
        m_data = MetadataDict(ids[i],
                                embedding,
                                chunks[i],
                                metadata["title"],
                                metadata["author"])
        data.append(m_data.to_dict())

    return data, file_name

def process_folder(client, folder_path):
    pdf_paths = get_pdf_files(folder_path)
    for path in pdf_paths:
        metadatas, document = process_file(str(path))
        client.add_document(document, metadatas)