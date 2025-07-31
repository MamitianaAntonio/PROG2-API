# main.py
from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenue sur FastAPI avec Starlette et Uvicorn!"}

@app.get("/hello/{nom}")
async def dire_bonjour(nom: str):
    return JSONResponse(content={"salutation": f"Bonjour {nom} ! 😄"})

