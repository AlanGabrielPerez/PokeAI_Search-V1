from fastapi import APIRouter, HTTPException
from app.schemas.pokemon import SearchResponse
from app.services.search_service import SearchService

router = APIRouter()

service = SearchService()


@router.get("/search", response_model=SearchResponse)
def search_pokemon_endpoint(query: str):

    if not query:
        raise HTTPException(status_code=400, detail="Por favor escribe algo para buscar.")

    return  service.search_pokemon(query)