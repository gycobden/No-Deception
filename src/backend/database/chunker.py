import pymupdf
from nltk.tokenize import sent_tokenize
import nltk
import re
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

def chunk_file(file_name, max_token_size=50):
    parsed_text = pymupdf.open(file_name)
    metadata = parsed_text.metadata

    title = metadata.get("title", "").strip()
    author = metadata.get("author", "").strip()

    # Fallbacks if title/author is empty or generic
    if not title or title.lower() in ["untitled", ""]:
        title = file_name.split("/")[-1]  # Use filename as fallback

    if not author or author.lower() in ["anonymous", ""]:
        author = "Unknown"

    metadata["title"] = title
    metadata["author"] = author

    raw_text = "\n".join(page.get_text("text") for page in parsed_text)

    # Normalize line breaks before chunking: replace line breaks with space, collapse multiple spaces
    raw_text = re.sub(r'\s*\n\s*', ' ', raw_text)  # remove inline newlines
    raw_text = re.sub(r'\s{2,}', ' ', raw_text).strip() 

    sentences = sent_tokenize(raw_text)
    chunks, current_chunk, ids, current_len = [], [], [], 0

    id_counter = 0
    id_prefix = file_name.split('/')[-1]
    for sent in sentences:
        tokens = sent.split()
        if current_len + len(tokens) > max_token_size:
            chunks.append(" ".join(current_chunk))
            ids.append(id_prefix + f"-{id_counter}")

            id_counter += 1
            current_chunk, current_len = [], 0

        current_chunk.append(sent)
        current_len += len(tokens)

    if current_chunk:
        chunks.append(" ".join(current_chunk))
        ids.append(id_prefix + f"-{id_counter}")
    return ids, chunks, metadata


if __name__ == "__main__":
    chunks, metadata = chunk_file("vaccine.pdf")
    print(chunks, metadata["title"], metadata["author"])



