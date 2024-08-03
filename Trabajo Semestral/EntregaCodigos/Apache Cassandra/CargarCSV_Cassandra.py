from cassandra.cluster import Cluster
import csv
from datetime import datetime
# https://www.kaggle.com/datasets/zakariaeyoussefi/cell-towers-worldwide-location-data-by-continent
# Conexión a Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('telecom')

# Función para insertar datos en la tabla cellTowers
def insert_cell_tower(row):
    query = """
    INSERT INTO cellTowers (Radio, MCC, MNC, LAC, CID, Longitude, Latitude, Range, Samples, Changeable, Created, Updated, AverageSignal)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    session.execute(query, (
        row['Radio'], int(row['MCC']), int(row['MNC']), int(row['LAC']), int(row['CID']),
        float(row['Longitude']), float(row['Latitude']), float(row['Range']), int(row['Samples']),
        bool(int(row['Changeable'])), datetime.strptime(row['Created'], "%Y-%m-%dT%H:%M:%SZ"),
        datetime.strptime(row['Updated'], "%Y-%m-%dT%H:%M:%SZ"), float(row['AverageSignal'])
    ))

# Función para insertar datos en la tabla countries
def insert_country(row):
    query = """
    INSERT INTO countries (MCC, Country, Continent)
    VALUES (%s, %s, %s)
    """
    session.execute(query, (int(row['MCC']), row['Country'], row['Continent']))

# Función para insertar datos en la tabla networks
def insert_network(row):
    query = """
    INSERT INTO networks (MCC, MNC, Network)
    VALUES (%s, %s, %s)
    """
    session.execute(query, (int(row['MCC']), int(row['MNC']), row['Network']))

# Leer el archivo CSV e insertar los datos en las tablas
file_path = 'Trabajo_Semestral_South_America.cellTowers.csv'

with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    inserted_countries = set()
    inserted_networks = set()
    
    for row in reader:
        insert_cell_tower(row)
        
        # Insertar en la tabla countries si no ha sido insertado antes
        if row['MCC'] not in inserted_countries:
            insert_country(row)
            inserted_countries.add(row['MCC'])
        
        # Insertar en la tabla networks si no ha sido insertado antes
        if (row['MCC'], row['MNC']) not in inserted_networks:
            insert_network(row)
            inserted_networks.add((row['MCC'], row['MNC']))

# Cerrar la conexión
cluster.shutdown()
