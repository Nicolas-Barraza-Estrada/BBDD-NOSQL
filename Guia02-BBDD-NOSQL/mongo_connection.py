from pymongo import MongoClient

def connect_to_mongodb():
    """
    Modificar aqui la dirección del servidor y el puerto, el nombre de la base de datos y la colección
    """
    client = MongoClient('localhost', 28017)
    db = client['pokeapi']
    collection = db['pokemon']
    return db, collection
