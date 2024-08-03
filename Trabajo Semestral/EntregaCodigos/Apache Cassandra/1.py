from cassandra.cluster import Cluster

# Conexión a Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('telecom')

# Consulta para obtener las proporciones de cada 
# tipo de red por país en Sudamérica
query_proportions = """
SELECT c.Country, t.Radio, COUNT(*) AS count, 
       (COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY c.Country)) 
        AS proportion
FROM cellTowers t
JOIN countries c ON t.MCC = c.MCC
WHERE c.Continent = 'South America'
GROUP BY c.Country, t.Radio;
"""

# Ejecutar la consulta
results = session.execute(query_proportions)

# Imprimir las proporciones
for row in results:
    print(f'Country: {row.country}, 
            Radio: {row.radio}, 
            Proportion: {row.proportion:.2%}')
