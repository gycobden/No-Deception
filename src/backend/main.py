from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StuffRequest(BaseModel):
    stuff1: int
    stuff2: int
    

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/calculate_stuff")
async def calculate_stuff(stuff_request: StuffRequest):
    stuff_request.stuff1
    stuff_request.stuff2

    message = {f"This is stuff by {stuff_request.stuff1}"}

    return {"message": message}