from neo4j import GraphDatabase
import csv

# Configuración de la conexión a Neo4j
uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

def create_cell_tower(tx, row):
    query = """
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
        created: $created,
        updated: $updated,
        averageSignal: toFloat($averageSignal)
    })
    """
    tx.run(query, row)

def create_relationships(tx, row):
    query = """
    MATCH (t:CellTower {CID: $CID})
    MATCH (c:Country {MCC: $MCC})
    MATCH (n:Network {MCC: $MCC, MNC: $MNC})
    MERGE (t)-[:LOCATED_IN]->(c)
    MERGE (t)-[:OPERATED_BY]->(n)
    """
    tx.run(query, row)

# Función principal para cargar los datos
def load_data(file_path):
    with driver.session() as session:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                session.write_transaction(create_cell_tower, row)
            # Separar la creación de relaciones en otra iteración
            file.seek(0)
            next(reader)  # Skip header row
            for row in reader:
                session.write_transaction(create_relationships, row)

# Ruta al archivo CSV
file_path = 'Trabajo_Semestral_Oceania.cellTowers.csv'

# Cargar los datos
load_data(file_path)

# Cerrar el controlador
driver.close()


Tipos de red
¿Cuál es la proporción de cada tipo de red, por país, en Sudamérica?

Cantidad de operadores
¿Cuáles son los países con mayor y menor cantidad de operadores en el mundo?
Progreso de países 
¿En qué países se han añadido la mayor y menor cantidad de torres en el último año?
¿De qué tipo fueron?


// Convierte las fechas almacenadas como strings a datetime
MATCH (t:CellTower)
SET t.Created = datetime(t.Created),
    t.Updated = datetime(t.Updated)



// Encuentra los países con la mayor cantidad de operadores
MATCH (c:Country)<-[:LOCATED_IN]-(t:CellTower)-[:OPERATED_BY]->(n:Network)
WITH c, COUNT(DISTINCT n) AS num_operators
RETURN c.Country AS Country, num_operators
ORDER BY num_operators DESC
LIMIT 1

UNION

// Encuentra los países con la menor cantidad de operadores
MATCH (c:Country)<-[:LOCATED_IN]-(t:CellTower)-[:OPERATED_BY]->(n:Network)
WITH c, COUNT(DISTINCT n) AS num_operators
RETURN c.Country AS Country, num_operators
ORDER BY num_operators ASC
LIMIT 1

//Consulta para el país con la mayor cantidad de torres añadidas en el último año:
WITH datetime() - duration({years: 1}) AS one_year_ago
MATCH (t:CellTower)-[:LOCATED_IN]->(c:Country)
WHERE t.Created >= one_year_ago
WITH c.Country AS country, COUNT(t) AS num_towers, COLLECT(t.Radio) AS types
ORDER BY num_towers DESC
WITH HEAD(collect({country: country, num_towers: num_towers, types: types})) AS result
RETURN result.country AS Country, result.num_towers AS Num_Towers, result.types AS Types

//Consulta para el país con la menor cantidad de torres añadidas en el último año
WITH datetime() - duration({years: 1}) AS one_year_ago
MATCH (t:CellTower)-[:LOCATED_IN]->(c:Country)
WHERE t.Created >= one_year_ago
WITH c.Country AS country, COUNT(t) AS num_towers, COLLECT(t.Radio) AS types
ORDER BY num_towers ASC
WITH HEAD(collect({country: country, num_towers: num_towers, types: types})) AS result
RETURN result.country AS Country, result.num_towers AS Num_Towers, result.types AS Types


//Consulta Cypher para Proporción de Cada Tipo de Red por País en Oceania
MATCH (t:CellTower)-[:LOCATED_IN]->(c:Country {Continent: "Oceania"})
WITH c, t.Radio AS network_type
WITH c, network_type, COUNT(*) AS count_per_type
MATCH (c)<-[:LOCATED_IN]-(t2:CellTower)
WITH c, network_type, count_per_type, COUNT(*) AS total_towers
RETURN c.Country AS Country,
       network_type AS Network_Type,
       count_per_type AS Count_Per_Type,
       total_towers AS Total_Towers,
       toFloat(count_per_type) / total_towers AS Proportion
ORDER BY c.Country, Proportion DESC
