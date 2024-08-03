from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client['Trabajo_Semestral_South_America']

# Consulta para obtener la proporción de cada tipo de red por país en America del Sur
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
        "$match": {
            "country_info.Continent": "South America"
        }
    },
    {
        "$group": {
            "_id": {
                "Country": "$country_info.Country",
                "Radio": "$radio"
            },
            "count": {"$sum": 1}
        }
    },
    {
        "$group": {
            "_id": "$_id.Country",
            "total": {"$sum": "$count"},
            "networks": {
                "$push": {
                    "radio": "$_id.Radio",
                    "count": "$count"
                }
            }
        }
    },
    {
        "$project": {
            "_id": 0,
            "Country": "$_id",
            "proportions": {
                "$map": {
                    "input": "$networks",
                    "as": "network",
                    "in": {
                        "radio": "$$network.radio",
                        "proportion": {"$divide": ["$$network.count", "$total"]}
                    }
                }
            }
        }
    }
]

proportions_by_country = list(db.cellTowers.aggregate(pipeline))
print(proportions_by_country)
