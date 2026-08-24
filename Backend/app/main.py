from fastapi import FastAPI
from app.routers import search

app = FastAPI(
    title="PokeAI Search",
    description="API que usa IA para buscar Pokémon por características",
    version="1.0.0"
)

app.include_router(search.router)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la PokeAI API. Ve a /docs para probarla."}