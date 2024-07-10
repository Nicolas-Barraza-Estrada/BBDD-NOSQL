from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient('mongodb://localhost:27017/')
db = client['Trabajo_Semestral']

pipeline = [
]

consulta = list(db.cellTowers.aggregate(pipeline))
print(consulta)










