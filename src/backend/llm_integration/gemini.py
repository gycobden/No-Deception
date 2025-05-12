# run in terminal for every new session
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/chidang/Downloads/gen-lang-client-0428886878-94e88900905a.json"

from tokenize import String
from google.cloud import bigquery
from google import generativeai as genai
from google.cloud import aiplatform
from backend.database.chroma_client import find_similar_documents
from sentence_transformers import SentenceTransformer

# configure gemini

model = genai.GenerativeModel("gemini-2.0-flash")

# embedder to convert user input 
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# example query
question = "What are the side effects of the Covid-19 vaccine?"
question_embedding = embedder.encode(question).tolist()

# search through database of research articles (return 5 results)
results = find_similar_documents(question_embedding, 5)
articles = results["documents"][0]
context = "\n".join(articles) # makes articles returned each on a new line so it's clearer

# make gemini answer the question with just info from our database
prompt = (
    "answer the question using only the information from the database \n" 
    + "context: " + context + "\n"
    + "question:" + question
)