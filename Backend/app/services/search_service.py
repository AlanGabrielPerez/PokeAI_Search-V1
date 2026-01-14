import os
import requests
import ast
from groq import Groq
from dotenv import load_dotenv
from app.schemas.pokemon import PokemonStats, PokemonDetail, SearchResponse

load_dotenv()

class SearchService:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)


    def _get_names_from_ai(self, user_query: str) -> list[str]:
        try:
            chat = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un experto en Pokémon. Tu trabajo es interpretar la búsqueda y devolver una lista de Python válida (['Pikachu', 'Charizard']). Responde SOLO con la lista. Máximo 6 pokémon. Nombres en inglés."
                    },
                    {
                        "role": "user",
                        "content": f"Genera una lista sobre: {user_query}. Ordenado por relevancia."
                    }
                ],
                temperature=0.5,
            )
            return ast.literal_eval(chat.choices[0].message.content)
        except Exception as e:
            print(f"Error en IA: {e}")
            return []


    def _get_pokemon_data(self, pokemon_name: str) -> PokemonDetail | None:
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower().strip()}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                
                stats_dict = {
                s["stat"]["name"].replace("-", "_"): s["base_stat"]
                for s in data["stats"]
            }
                pokemon_stats = PokemonStats(
                    hp=stats_dict["hp"],
                    attack=stats_dict["attack"],
                    defense=stats_dict["defense"],
                    special_attack=stats_dict["special_attack"],
                    special_defense=stats_dict["special_defense"],
                    speed=stats_dict["speed"],
                )
                
                return PokemonDetail(
                    name=data['name'],
                    types=[t['type']['name'] for t in data['types']],
                    image=data['sprites']['front_default'] or "",
                    abilities=[a['ability']['name'] for a in data['abilities'][:5]],
                    stats=pokemon_stats,
                )
            return None
        except Exception:
            return None
        
        

    def search_pokemon(self, query: str) -> SearchResponse:
        
        ai_names = self._get_names_from_ai(query)
        
        valid_pokemons = []

        for name in ai_names:
            details = self._get_pokemon_data(name)
            if details:
                valid_pokemons.append(details)
        
        
        return SearchResponse(
            total=len(valid_pokemons),
            pokemons=valid_pokemons
        )