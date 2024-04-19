import requests
from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient('localhost', 28017)
db = client['pokeapi']  # Nombre de la base de datos
collection = db['pokemon']  # Nombre de la colección

# URL base de la PokeAPI
base_url = 'https://pokeapi.co/api/v2/'

# Función para extraer los datos de la PokeAPI y almacenarlos en MongoDB
def extract_and_store_pokemon_data():
    try:
        # Lista para almacenar los datos de los Pokémon
        pokemon_data_list = []
        
        # Rangos de IDs de Pokémon
        ranges = [(1, 1025), (10001, 10277)]
        
        for range_start, range_end in ranges:
            # Iterar sobre cada rango de IDs
            for pokemon_id in range(range_start, range_end + 1):
                pokemon_url = base_url + f'pokemon/{pokemon_id}'
                pokemon_response = requests.get(pokemon_url)
                if pokemon_response.status_code == 200:
                    pokemon_data = pokemon_response.json()
                    pokemon_data_list.append(pokemon_data)
                    print(f"Pokemon {pokemon_data['name']} insertado en la lista.")
                else:
                    print(f"No se pudo obtener los datos del Pokémon con ID {pokemon_id}.")
        
        # Insertar los datos de los Pokémon en la base de datos MongoDB
        if pokemon_data_list:
            collection.insert_many(pokemon_data_list)
            print("Todos los Pokémon fueron insertados en la base de datos.")
        else:
            print("No se obtuvieron datos de Pokémon para insertar.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Ejecutar la función para extraer y almacenar los datos
extract_and_store_pokemon_data()
