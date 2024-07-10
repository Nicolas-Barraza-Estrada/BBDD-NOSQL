import pandas as pd
from pymongo import MongoClient

# Leer el archivo CSV
csv_file = 'archive/modified_Oceania_towers.csv'
df = pd.read_csv(csv_file)

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:28017/')
db = client['Trabajo_Semestral']

# Crear índices únicos en las colecciones `countries` y `networks`
db.countries.create_index([("MCC", 1)], unique=True)
db.networks.create_index([("MCC", 1), ("MNC", 1)], unique=True)

chunksize = 10000  # Número de filas por chunk
for chunk in pd.read_csv(csv_file, chunksize=chunksize):
    # Procesar países
    countries = chunk[['MCC', 'Country', 'Continent']].drop_duplicates()
    for _, country in countries.iterrows():
        db.countries.update_one(
            {"MCC": country['MCC']},
            {"$set": {"Country": country['Country'], "Continent": country['Continent']}},
            upsert=True
        )

    # Procesar redes
    networks = chunk[['MCC', 'MNC', 'Network']].drop_duplicates()
    for _, network in networks.iterrows():
        db.networks.update_one(
            {"MCC": network['MCC'], "MNC": network['MNC']},
            {"$set": {"Network": network['Network']}},
            upsert=True
        )

    # Obtener referencias a `countries` y `networks`
    countries_dict = {country['MCC']: db.countries.find_one({"MCC": country['MCC']})['_id'] for _, country in countries.iterrows()}
    networks_dict = {(network['MCC'], network['MNC']): db.networks.find_one({"MCC": network['MCC'], "MNC": network['MNC']})['_id'] for _, network in networks.iterrows()}

    # Procesar cellTowers con referencias
    cell_towers = []
    for _, row in chunk.iterrows():
        idCountry = countries_dict.get(row['MCC'])
        idNetwork = networks_dict.get((row['MCC'], row['MNC']))
        if idCountry and idNetwork:
            cell_towers.append({
                'radio': row['radio'],
                'MCC': row['MCC'],
                'MNC': row['MNC'],
                'TAC': row['TAC'],
                'CID': row['CID'],
                'LON': row['LON'],
                'LAT': row['LAT'],
                'RANGE': row['RANGE'],
                'SAM': row['SAM'],
                'changeable': row['changeable'],
                'created': row['created'],
                'updated': row['updated'],
                'averageSignal': row['averageSignal'],
                'idCountry': idCountry,
                'idNetwork': idNetwork
            })

    # Insertar cellTowers
    if cell_towers:
        db.cellTowers.insert_many(cell_towers)

print("Datos insertados correctamente en chunks")
