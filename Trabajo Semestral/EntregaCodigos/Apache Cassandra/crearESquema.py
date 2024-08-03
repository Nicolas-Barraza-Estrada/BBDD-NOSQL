from cassandra.cluster import Cluster

# Conexión a Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Crear el keyspace si no existe
session.execute("""
CREATE KEYSPACE IF NOT EXISTS telecom
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
""")

# Seleccionar el keyspace
session.set_keyspace('telecom')

# Crear la tabla cellTowers
session.execute("""
CREATE TABLE IF NOT EXISTS cellTowers (
    Radio text,
    MCC int,
    MNC int,
    LAC int,
    CID int,
    Longitude float,
    Latitude float,
    Range float,
    Samples int,
    Changeable boolean,
    Created timestamp,
    Updated timestamp,
    AverageSignal float,
    PRIMARY KEY ((MCC, MNC, LAC, CID))
)
""")

# Crear la tabla countries
session.execute("""
CREATE TABLE IF NOT EXISTS countries (
    MCC int PRIMARY KEY,
    Country text,
    Continent text
)
""")

# Crear la tabla networks
session.execute("""
CREATE TABLE IF NOT EXISTS networks (
    MCC int,
    MNC int,
    Network text,
    PRIMARY KEY ((MCC, MNC))
)
""")

# Cerrar la conexión
cluster.shutdown()
