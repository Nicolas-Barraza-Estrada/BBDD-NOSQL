from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client['Trabajo_Semestral_Oceania']

pipeline = [
    # Añadir un campo combinado de MCC y MNC en cellTowers
    {
        "$addFields": {
            "combined_MCC_MNC": {"$concat": [{"$toString": "$MCC"}, "_", {"$toString": "$MNC"}]}
        }
    },
    # Añadir un campo combinado de MCC y MNC en networks
    {
        "$lookup": {
            "from": "networks",
            "let": {"combined_MCC_MNC": "$combined_MCC_MNC"},
            "pipeline": [
                {
                    "$addFields": {
                        "combined_MCC_MNC": {"$concat": [{"$toString": "$MCC"}, "_", {"$toString": "$MNC"}]}
                    }
                },
                {
                    "$match": {
                        "$expr": {"$eq": ["$combined_MCC_MNC", "$$combined_MCC_MNC"]}
                    }
                }
            ],
            "as": "network_info"
        }
    },
    {
        "$unwind": "$network_info"
    },
    {
        "$group": {
            "_id": {"MCC": "$MCC", "MNC": "$MNC"},
            "countries": {"$addToSet": "$network_info.MCC"}
        }
    },
    {
        "$match": {
            "countries.1": {"$exists": True}
        }
    }
]

operators_in_multiple_countries = list(db.cellTowers.aggregate(pipeline))
print(operators_in_multiple_countries)
