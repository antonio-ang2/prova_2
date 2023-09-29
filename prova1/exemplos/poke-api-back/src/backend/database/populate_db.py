import pymongo
import requests
import json

def populate_db():
    # Conectar ao servidor MongoDB
    client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
    db = client["pokemon_db"]
    collection = db["pokemon_collection"]

    # Fazer a requisição à API da PokeAPI
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
    data = response.json()

    # Iterar sobre os resultados e inserir os dados no banco de dados
    for result in data["results"]:
        name = result["name"]
        url = result["url"]
        pokemon_id = int(url.split("/")[-2])  # Extrair o ID do URL

        # Obter mais informações do Pokemon usando o URL
        pokemon_response = requests.get(url)
        pokemon_data = pokemon_response.json()
        
        sprites = pokemon_data["sprites"]

        # Criar um registro com os campos desejados
        record = {
            "name": name,
            "id": pokemon_id,
            "sprites": sprites
        }

        # Inserir o registro na coleção
        collection.insert_one(record)

    print("Dados inseridos no banco de dados!")

if __name__ == "__main__":
    populate_db()
