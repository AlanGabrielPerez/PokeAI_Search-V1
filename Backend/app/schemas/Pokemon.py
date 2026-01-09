from pydantic import BaseModel
from typing import List

class PokemonRequests(BaseModel):
    query: str

class PokemonStat(BaseModel):
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


class PokemonDetail(BaseModel):
    
    name: str
    img: str
    type: List[str]
    abilities: List[str]
    stats: PokemonStat
    
class SearchPokemonResponse(BaseModel):
    total: int
    pokemon: List[PokemonDetail]