import requests

def prueba_consola(nombrePokemon):
    url= f'https://pokeapi.co/api/v2/pokemon/{nombrePokemon}'
    response = requests.get(url)
    
    if response.status_code == 200:
        
        pokemon_data = response.json()
        
        nombre = pokemon_data['name']
        print(F'Nombre:{nombre.capitalize()}')
        
        tipos = [tipo['type']['name'] for tipo in pokemon_data['types']]
        print(f'\nTipos:{', '.join(tipos).capitalize()}')
        
        print('\nEstadísticas:')
        for estadistica in pokemon_data['stats']:
            stat_name = estadistica['stat']['name']
            stat_value = estadistica['base_stat']
            print(f'{stat_name.capitalize()}: {stat_value}')
        
        habilidades= [habilidad['ability']['name'] for habilidad in pokemon_data['abilities']]
        print(f'\nHabilidades: {', '.join(habilidades).capitalize()}')
        
        print('\nMovimientos:')
        movimientos = [movimiento['move']['name'] for movimiento in pokemon_data['moves'][:5]]
        print(f'{', '.join(movimientos).capitalize()}')
        
        sprites = pokemon_data['sprites']['front_default']
        print(f'\nImagen del Pokémon: {sprites}')
        
    else:
        print('Pokémon no encontrado. Por favor, verifica el nombre e intenta de nuevo.')
        
if __name__ == "__main__":
    nombrePokemon = input('Ingresa el nombre del Pokémon: ').lower()
    prueba_consola(nombrePokemon)