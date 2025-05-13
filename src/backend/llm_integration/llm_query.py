from google import genai
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

# Set up Gemini client
gemini_client = genai.Client(api_key="AIzaSyBd-XDQ3LWeuHTL3Wb3KPY9TZGuZAZ1Fag")

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
    response = gemini_client.models.generate_content(
        model="gemini-2.0-flash",
        contents=
            "Here is the correct information:\n" +
            database_text +
            "\nHere is some user text:\n" +
            user_text +
            "\nCan you compare the user text to the correct information and " +
            "do a similarity comparison? If the user text is extremely different, " +
            "show those sentences from the user text and give it a category of 'bad' " +
            "if it is similar give it a category of 'good'. Just give me the highligted sentences and the category no need to summarize",
            config={
        "response_mime_type": "application/json",
        "response_schema": list[Analysis]
            },
    )
    article_analysis: list[Analysis] = response.parsed
    return article_analysis

pprint.pprint(queryLLM_to_JSON(user_text))