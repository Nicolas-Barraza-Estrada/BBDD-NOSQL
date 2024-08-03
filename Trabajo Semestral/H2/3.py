from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client['Trabajo_Semestral_Oceania']

# Calcula la fecha de hace un año
one_year_ago = datetime.now() - timedelta(days=(365*1))
one_year_ago_iso = one_year_ago.isoformat()
# Consulta para obtener la cantidad de torres añadidas en el ultimo año
pipeline = [
    {"$match": {
        "created": {"$gte": one_year_ago_iso}
        }
    },
    {"$group": {
        "_id": {"idCountry": "$idCountry", "radio": "$radio"},
        "count": {"$sum": 1}
    }
    },
    {"$group": {
        "_id": "$_id.idCountry",
        "total": {"$sum": "$count"},
        "networks": {"$push": {"type": "$_id.radio", "count": "$count"}}
    }
    },
    
    {"$sort": {"total": -1}}
]

result = list(db.cellTowers.aggregate(pipeline))

if result:
    print("País con mayor cantidad de torres añadidas:", result[0])
    print("País con menor cantidad de torres añadidas:", result[-1])
    
    # Obtener nombres de países
    for doc in result:
        country = db.countries.find_one({"_id": doc['_id']})
        doc['Country'] = country['Country'] if country else 'Desconocido'
        
    print("Detalles:")
    for doc in result:
        print(f"País: {doc['Country']}, Total: {doc['total']}")
        for network in doc['networks']:
            print(f"  Tipo: {network['type']}, Cantidad: {network['count']}")
