# Author: Ozzie Farfan
# Reads all recipies from MongoDB ordered by calories

import json
from time import sleep
from kafka import KafkaConsumer

# MongoDB libraries
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
collection = db.recipies

def find_recipie_db(a_title):
    found = False
    mysearch = collection.find_one({'title':a_title})
    if mysearch != '':
        pprint(mysearch)
        found = True
    return found


if __name__ == '__main__':
    for myrecipie in collection.find().sort('calories'):
        print('{:30}\t\t {}\t {}\t'.format(myrecipie['title'],myrecipie['submitter'],myrecipie['calories']))


