import pandas as pd
from pymongo import MongoClient
# https://www.kaggle.com/datasets/zakariaeyoussefi/cell-towers-worldwide-location-data-by-continent
# Configuración de MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Trabajo_Semestral']

# Crear índices únicos en las colecciones `countries` y `networks`
db.countries.create_index([("MCC", 1)], unique=True)
db.networks.create_index([("MCC", 1), ("MNC", 1)], unique=True)

def process_csv(file_path):
    chunksize = 10000  # Número de filas por chunk
    path = ' '
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        if path != file_path:
            print(f"Procesando archivo: {file_path}")
        path = file_path
        # Convertir los valores del DataFrame a tipos nativos de Python
        chunk = chunk.astype(object).where(pd.notnull(chunk), None)
        
        # Procesar países
        countries = chunk[['MCC', 'Country', 'Continent']].drop_duplicates()
        for _, country in countries.iterrows():
            db.countries.update_one(
                {"MCC": country['MCC']},
                {"$set": {"Country": country['Country'], "Continent": country['Continent']}},
                upsert=True
            )

        # Procesar redes(empresas)
        networks = chunk[['MCC', 'MNC', 'Network']].drop_duplicates()
        for _, network in networks.iterrows():
            db.networks.update_one(
                {"MCC": network['MCC'], "MNC": network['MNC']},
                {"$set": {"Network": network['Network']}},
                upsert=True
            )

        # Obtener referencias a `countries` y `networks`
        countries_dict = {country['MCC']: db.countries.find_one
                          ({"MCC": country['MCC']})['_id'] for _, country in countries.iterrows()}
        networks_dict = {(network['MCC'], network['MNC']): db.networks.find_one(
            {"MCC": network['MCC'], "MNC": network['MNC']})['_id'] for _, network in networks.iterrows()}

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

# Lista de archivos CSV para procesar
csv_files = [
    'archive/modified_Africa_towers.csv',
    'archive/modified_Oceania_towers4.csv',
    'archive/modified_Asia_towers.csv',
    'archive/modified_Europe_towers.csv',
    'archive/modified_NorthAmerica_towers.csv',
    'archive/modified_South_America_towers.csv'
    # Añadir más archivos CSV según sea necesario
]

# Procesar cada archivo CSV
for csv_file in csv_files:
    process_csv(csv_file)

print("Datos insertados correctamente para todos los archivos CSV")
