from fastapi import FastAPI
from pydantic import BaseModel
# from backend.llm_integration import generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow extension to call backend (CORS)
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["chrome-extension://<your-extension-id>"],
    allow_origins=[
        "chrome-extension://jnlfehcpklhnldhimhdfkkclghofickd",
        "http://localhost:3000",  # Add your frontend's URL here
        "https://your-beta-frontend-url.com"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(prompt_req: PromptRequest):
    # return {"response": generate_response(prompt_req.prompt)}
    return {"hello"}