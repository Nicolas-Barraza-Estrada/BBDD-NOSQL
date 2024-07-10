from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client['Trabajo_Semestral_Oceania']
# no va
# Calcula la fecha de hace un año
one_year_ago = datetime.now() - timedelta(days=(365*1))
one_year_ago_iso = one_year_ago.isoformat()

# Consulta para obtener el tipo d torres añadidas en el último año
pipeline = [
    {
        "$match": {
            "created": {"$gte": one_year_ago}
        }
    },
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
            "_id": {
                "Country": "$country_info.Country",
                "Radio": "$radio"
            },
            "new_towers": {"$sum": 1}
        }
    },
    {
        "$sort": {"new_towers": -1}
    }
]

new_towers_by_type = list(db.cellTowers.aggregate(pipeline))
print(new_towers_by_type)
