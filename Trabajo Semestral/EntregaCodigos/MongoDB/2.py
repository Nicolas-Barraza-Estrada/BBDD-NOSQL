from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client['Trabajo_Semestral_South_America']

#Obitiene la cantidad de operadores por pais
pipeline = [
    {
        "$lookup": {
            "from": "countries",
            "localField": "MCC",
            "foreignField": "MCC",
            "as": "country_info"
        }
    },
    {
        "$unwind": "$country_info"
    },
    {
        "$group": {
            "_id": "$country_info.Country",
            "num_operators": {"$addToSet": "$MNC"}
        }
    },
    {
        "$project": {
            "_id": 1,
            "num_operators": {"$size": "$num_operators"}
        }
    },
    {
        "$sort": {"num_operators": -1}
    }
]

operator_counts = list(db.cellTowers.aggregate(pipeline))
print(operator_counts[:5])  # Países con mayor cantidad de operadores
print(operator_counts[-5:])  # Países con menor cantidad de operadores
