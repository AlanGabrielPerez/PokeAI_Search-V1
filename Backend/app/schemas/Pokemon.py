from pydantic import BaseModel
from typing import List

class PokemonRequests(BaseModel):
    query: str

class PokemonStats(BaseModel):
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


class PokemonDetail(BaseModel):
    
    name: str
    image: str
    types: List[str]
    abilities: List[str]
    stats: PokemonStats
    
class SearchResponse(BaseModel):
    total: int
    pokemons: List[PokemonDetail]