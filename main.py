from fastapi import FastAPI, Request
from pydantic import BaseModel
from bot import get_dra_response



app = FastAPI(Title =  'DRA API',
              description='API for Data Retrieval Agent (DRA) using Cohere LLM',
                version='1.0.0')


@app.get("/")
def read_root():
    return {"message": "Welcome to the DRA API. Use /dra_response to get a response from the DRA."}

@app.post("/dra_response")
async def dra_response(request: Request):
    body = await request.json()
    query = body.get("query", "").strip()

    if not query:
        return {"error": "Consulta vacía o no proporcionada."}

    response_text = get_dra_response(query)
    return {"response": response_text}