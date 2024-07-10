from pymongo import MongoClient

# Configuración de MongoDB
client = MongoClient('mongodb://localhost:28017/')
db = client['Trabajo_Semestral_Full']

# Definir los límites de coordenadas
bounding_boxes = [
    {
        "min_lat": -36.853493,
        "max_lat": -36.776671,
        "min_lon": -73.076652,
        "max_lon": -73.059657
    },
    {
        "min_lat": -36.834673,
        "max_lat": -36.766633,
        "min_lon": -73.007987,
        "max_lon": -73.001121
    }
]

# Función para contar torres en un rango de coordenadas
def count_towers_in_bbox(bbox):
    count = db.cellTowers.count_documents({
        "MCC": 730,
        "LAT": {"$gte": bbox["min_lat"], "$lte": bbox["max_lat"]},
        "LON": {"$gte": bbox["min_lon"], "$lte": bbox["max_lon"]}
    })
    return count

# Contar torres en cada rango de coordenadas
total_towers = 0
for bbox in bounding_boxes:
    count = count_towers_in_bbox(bbox)
    print(f"Torres en el rango {bbox}: {count}")
    total_towers += count

print(f"Total de torres en los rangos especificados: {total_towers}")
