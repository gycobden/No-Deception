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

# Embed user text
embedding = embed_chunk(user_text).tolist()

# Access Chroma DB
chroma_client = ChromaClient(config.CHROMA_PATH, config.COLLECTION_NAME)
similar_text_chunks = chroma_client.find_similar_documents(embedding, 5)
database_text = "\n".join([meta["text_chunk"] for meta in similar_text_chunks["metadatas"][0]])

# Response type Object
class Analysis(BaseModel):
    highlight_sentences: list[str]
    category: str

# Query Gemini LLM
def queryLLM_to_JSON(user_text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(
        [
            "Here is information from trustworthy documents:\n" + database_text +
            "\nHere is some user text:\n" + user_text +
            "\nCan you compare the user text to the correct information and " +
            "do a similarity comparison? If the user text is extremely different, " +
            "show those sentences from the user text labeled as 'sentence' and give it a category of 'bad' " +
            "if it is similar give it a category of 'good'. Just give me the highlighted sentences and the category no need to summarize"
        ],
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