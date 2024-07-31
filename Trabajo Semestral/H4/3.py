from cassandra.cluster import Cluster
from datetime import datetime, timedelta

# Conexión a Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('telecom')

# Calcular la fecha de hace un año desde hoy
one_year_ago = datetime.now() - timedelta(days=365)

# Consulta para obtener el número de torres añadidas 
# en el último año por país y tipo de red
query_towers_by_country = """
SELECT c.Country, t.Radio, COUNT(*) AS num_towers
FROM cellTowers t
JOIN countries c ON t.MCC = c.MCC
WHERE t.Created >= %s
GROUP BY c.Country, t.Radio;
"""

# Ejecutar la consulta
rows = session.execute(query_towers_by_country, [one_year_ago])

# Convertir los resultados a una lista para facilitar el manejo
country_tower_counts = {}
for row in rows:
    country = row.country
    radio = row.radio
    num_towers = row.num_towers
    if country not in country_tower_counts:
        country_tower_counts[country] = {}
    country_tower_counts[country][radio] = num_towers

# Ordenar por número de torres en orden descendente y ascendente
country_tower_totals = [(country, sum(radio_counts.values())) for 
                        country, radio_counts in country_tower_counts.items()]
country_tower_totals_sorted_desc = sorted(country_tower_totals, 
                                          key=lambda x: x[1], reverse=True)
country_tower_totals_sorted_asc = sorted(country_tower_totals, 
                                         key=lambda x: x[1])

# Obtener los países con la mayor y menor cantidad de torres
country_with_most_towers = country_tower_totals_sorted_desc[0:5]
country_with_least_towers = country_tower_totals_sorted_asc[0:5]

# Imprimir todos los resultados
print("Country with most towers:")
for country, num_towers in country_with_most_towers:
    print(f"{country}: {num_towers} towers")
print()
print("Country with least towers:")
for country, num_towers in country_with_least_towers:
    print(f"{country}: {num_towers} towers")



