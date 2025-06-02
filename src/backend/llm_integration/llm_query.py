import google.generativeai as genai
import sys, os
# Add project root (for config.py)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
# Add src/ (for backend.database.* modules)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from backend.database.chroma_client import ChromaClient
from backend.database.embedder import embed_chunk
from pydantic import BaseModel
import config
import pprint
import json

user_text = "vaccines are bad and cause autism"

# api key to use when local

genai.configure(api_key=os.getenv("GENAI_API_KEY"))
gemini_client = genai

# Response type Object
class Analysis(BaseModel):
    highlight_sentences: list[str]
    category: str

# Query Gemini LLM
def queryLLM_to_JSON(user_text):
    # Embed user text
    embedding = embed_chunk(user_text).tolist()

    # Access Chroma DB
    # if not config.REMOTE_ACCESS:
    chroma_client = ChromaClient({'db_dir': config.CHROMA_PATH},
                                    config.COLLECTION_NAME,
                                    remote=False)
    # else:
    #     chroma_client = ChromaClient({'host': config.REMOTE_ADDRESS, 'port': config.REMOTE_PORT},
    #                                  config.COLLECTION_NAME, remote=True)
    similar_text_chunks = chroma_client.find_similar_documents(embedding, 5)

    print("stc: ", similar_text_chunks)

    database_text = "\n".join([doc for doc in similar_text_chunks["documents"][0]])

    print("database text: ", database_text)

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = (
    "Here is information from trustworthy documents:\n" + database_text +
    "\nHere is some user text:\n" + user_text +
    "\nCompare the user text to the trustworthy information above. " +
    "For each sentence in the user text that does not align with the trustworthy documents, " +
    "include it in the output as an object with two fields: 'sentence' (the sentence string) and 'category' (either 'misleading' or 'infactual'). " +
    "Use 'misleading' if the sentence is partially true or could be interpreted incorrectly, and 'infactual' if the sentence is factually incorrect or contradicts the trustworthy documents. " +
    "After processing all sentences, assign an overall 'category' to the user text, choosing one of: 'couldn't find relevant documents', 'bad', or 'good'.\n" +
    "Criteria:\n"
    " - good: text aligns with claims in the document\n"
    " - bad: text contradicts facts in the document\n"
    " - couldn't find relevant documents: text does not align with any trustworthy document text\n"
    "Return ONLY a JSON object with two fields:\n"
    "  'sentences': a list of the untrustworthy sentences (strings),\n"
    "  'category': the overall category (string).\n"
    "Example 1:\n"
    "{\n"
    '  "sentences": [\n'
    '    {"sentence": "Sentence 1 that is misleading.", "category": "misleading"},\n'
    '    {"sentence": "Sentence 2 that is factually incorrect.", "category": "infactual"}\n'
    "  ],\n"
    '  "category": "bad"\n'
    "}\n"
    "Example 2:\n"
    "{\n"
    '  "sentences": [],\n'
    '  "category": "couldn\'t find relevant documents"\n'
    "}\n"
    )

    response = model.generate_content(
        [prompt],
        generation_config={
            "response_mime_type": "application/json",
            # Add other config options as needed
        }
    )

    print("Raw LLM response:", response.text)

    relevant_articles = list(set(
        (meta["source_title"], meta["source_author"])
        for meta in similar_text_chunks["metadatas"][0]))

    # Parse the JSON response text
    article_analysis = json.loads(response.text)

    return article_analysis, relevant_articles

pprint.pprint(queryLLM_to_JSON(user_text))