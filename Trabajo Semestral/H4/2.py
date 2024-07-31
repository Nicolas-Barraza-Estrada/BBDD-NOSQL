from cassandra.cluster import Cluster

# Conexión a Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('telecom')

# Consulta para obtener el número de operadores por país
query_operators_by_country = """
SELECT c.Country, COUNT(DISTINCT n.Network) AS num_operators
FROM cellTowers t
JOIN countries c ON t.MCC = c.MCC
JOIN networks n ON t.MCC = n.MCC
GROUP BY c.Country;
"""

# Ejecutar la consulta
rows = session.execute(query_operators_by_country)

# Convertir los resultados a una lista para facilitar el manejo
country_operator_counts = []
for row in rows:
    country_operator_counts.append((row.country, row.num_operators))

# Ordenar por número de operadores en orden descendente y ascendente
country_operator_counts_sorted_desc = sorted(
    country_operator_counts, key=lambda x: x[1], reverse=True)
country_operator_counts_sorted_asc = sorted(
    country_operator_counts, key=lambda x: x[1])

# Obtener los países con la mayor y menor cantidad de operadores
country_with_most_operators = country_operator_counts_sorted_desc[0:5]
country_with_least_operators = country_operator_counts_sorted_asc[0:5]

# Imprimir los resultados
print("Country with most operators:")
for country, num_operators in country_with_most_operators:
    print(f"{country}: {num_operators} operators")
print()
print("Country with least operators:")
for country, num_operators in country_with_least_operators:
    print(f"{country}: {num_operators} operators")


