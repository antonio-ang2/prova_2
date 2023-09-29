from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Conectar ao banco de dados MongoDB
client = MongoClient("mongodb://root:example@localhost:27017/")
db = client["pokemon_db"]
collection = db["pokemon_collection"]

@app.route("/")
def home():
    return "Welcome to the Pokémon API!"

@app.route("/pokemon/<pokemon_name>")
def get_pokemon(pokemon_name):
    pokemon = collection.find_one({"name": pokemon_name}, {"_id": 0})

    if pokemon:
        return jsonify(pokemon)
    else:
        return jsonify({"error": "Pokemon not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
