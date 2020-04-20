from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
collection = db.cities


