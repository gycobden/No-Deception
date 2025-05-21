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

user_text = "Vaccines train your immune system to create antibodies, just as it does when it's exposed to a disease. However, because vaccines contain only killed or weakened forms of germs like viruses or bacteria, they do not cause the disease or put you at risk of its complications."

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
    chroma_client = ChromaClient(config.CHROMA_PATH, config.COLLECTION_NAME)
    similar_text_chunks = chroma_client.find_similar_documents(embedding, 5)

    print("stc: ", similar_text_chunks)

    database_text = "\n".join([meta["text_chunk"] for meta in similar_text_chunks["metadatas"][0]])

    print("database text: ", database_text)

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = (
    "Here is information from trustworthy documents:\n" + database_text +
    "\nHere is some user text:\n" + user_text +
    "\nCompare the user text to the trustworthy information above. " +
    "For each sentence in the user text, if it contains information that directly conflicts with the given documents, " +
    "include it in the output as a string. If it contains information that does not directly" +
    "conflict with the documents, do not add it." + 
    "Then, assign an overall 'category' to the user text, choosing one of: 'couldn't find relevant documents', 'bad', or 'good'.\n" +
    "Criteria:\n"
    " - good: text aligns with claims in the document\n"
    " - bad: text contradicts facts in the document\n"
    " - couldn't find relevant documents: text does not align with any trustworthy document text\n"
    "Return ONLY a JSON object with two fields:\n"
    "  'sentences': a list of the untrustworthy sentences (strings),\n"
    "  'category': the overall category (string).\n"
    "Example:\n"
    "{\n"
    '  "sentences": ["Sentence 1 that is different.", "Sentence 2 that is different."],\n'
    '  "category": "bad"\n'
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