# Author: Ozzie Farfan
# This is an example with the Basic commands to MongoDB 
# Este ejemplo sirve para verificar que tenemos acceso al Contenedor de MongoDB

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
collection = db.cities

pprint(collection)
print ("\nColecciones disponibles")
pprint(db.list_collection_names())

print("\nlistado de coleccion: cities")
mycities = collection.find()
for a in mycities:
   pprint(a)

print("\nBusca un documento. Si no existe, entonces lo inserta")
unique = False
a_city = {'name': 'Toronto', 'country': 'Canada'}
mysearch = collection.find_one(a_city)
if mysearch != '':
    print ("Encontre..")
    pprint(mysearch)
else:
    # no lo encontro
    unique = True

if unique == True:
    print("\ninsertando a la coleccion")
    postid = collection.insert_one(a_city).inserted_id
    print("inserted id: ", postid)

