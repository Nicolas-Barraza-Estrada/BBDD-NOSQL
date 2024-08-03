from neo4j import GraphDatabase
import csv
from datetime import datetime
# https://www.kaggle.com/datasets/zakariaeyoussefi/cell-towers-worldwide-location-data-by-continent
# Configuración de la conexión a Neo4j
uri = "bolt://localhost:7687"
user = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(user, password))

def create_cell_tower_with_relationships(tx, row):
    query = """
    MERGE (c:Country {MCC: $MCC})
    MERGE (n:Network {MCC: $MCC, MNC: $MNC})
    CREATE (t:CellTower {
        Radio: $radio,
        MCC: $MCC,
        MNC: $MNC,
        TAC: $TAC,
        CID: $CID,
        LON: toFloat($LON),
        LAT: toFloat($LAT),
        RANGE: toFloat($RANGE),
        SAM: toInteger($SAM),
        changeable: $changeable,
        Created: datetime($created),
        Updated: datetime($updated),
        AverageSignal: toFloat($averageSignal)
    })
    MERGE (t)-[:LOCATED_IN]->(c)
    MERGE (t)-[:OPERATED_BY]->(n)
    """
    tx.run(query, row)

def load_data(file_path):
    with driver.session() as session:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                session.write_transaction(create_cell_tower_with_relationships, row)

# Ruta al archivo CSV
file_path = 'Trabajo_Semestral_South_America.cellTowers.csv'

# Cargar los datos
load_data(file_path)

# Cerrar el controlador
driver.close()
