import os
from dotenv import load_dotenv
from groq import Groq

#Cargar configuracion
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def get_pokemon_list():
   
    consulta_usuario = input("\nIngresa características de los Pokémon que deseas buscar")

    print("\nBuscando Pokémon...")

    try:
        chat_completion = client.chat.completions.create(
            
            model="llama-3.3-70b-versatile",
               
            messages=[
                {
                    "role": "system",
                    "content": "Eres un experto en Pokémon. Tu trabajo es interpretar la busqueda del usuario (incluso si tiene errores ortograficos) y devolver una lista de Python válida (['Nombre1', 'Nombre2']). Responde SOLO con la lista. Nombres en inglés."
                },
                {
                    "role": "user",
                    "content": f"Genera una lista de 10 o menos elementos sobre: {consulta_usuario}. Ordenado por relevancia."
                }
            ],
            temperature=0.5,
        )

        respuesta = chat_completion.choices[0].message.content
        
        print("-" * 30)
        print(respuesta)
        print("-" * 30)
        
        
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    get_pokemon_list()