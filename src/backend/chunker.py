import pymupdf
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt_tab')

"""
Parses the given PDF file into text using PyMuPDF's layout based parsing
and divide them in semantically meaningful text chunks using tokenizers
from nltk.

Args:
    file_name: The name of the PDF File to be parsed and chunked
    max_token_size: The max token size of a text chunk.
Returns:
    chunks: List of text chunks, the source article which these chunks belongs to
            and the author of that source article.
"""

def chunk_file(file_name, max_token_size=200):
    parsed_text = pymupdf.open(file_name)
    raw_text = "\n".join(page.get_text("text") for page in parsed_text)

    sentences = sent_tokenize(raw_text)
    chunks, current_chunk, ids, current_len = [], [], [], 0

    id_counter = 0
    for sent in sentences:
        tokens = sent.split()
        if current_len + len(tokens) > max_token_size:
            chunks.append(" ".join(current_chunk))
            ids.append(file_name + f"-{id_counter}")

            id_counter += 1
            current_chunk, current_len = [], 0

        current_chunk.append(sent)
        current_len += len(tokens)

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return ids, chunks, parsed_text.metadata


if __name__ == "__main__":
    chunks, metadata = chunk_file("vaccine.pdf")
    print(chunks, metadata["title"], metadata["author"])



