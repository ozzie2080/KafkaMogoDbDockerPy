#! python3
# @(#) consumer_save.py : Reads recipies from Kafka and save them in MongoDB 
# @(#)                    Sends email if new records are created
# @(#) Author: Ozzie Farfan

import json
from time import sleep
import sys
import os
from kafka import KafkaConsumer
from sendemail import send_alert

# MongoDB libraries
from pymongo import MongoClient
from pprint import pprint

# Read environment variables
try:
    KAFKA_HOST=os.getenv('KAFKA_HOST','localhost:9092')
except KeyError:
    print ("please set the env. variable for KAFKA_HOST")

output_file="alert.txt"

print ("using KAFKA_HOST = ",KAFKA_HOST)

# connects to database
try:
   client = MongoClient('mongodb://localhost:27017/')
   db = client.mydb
   collection = db.recepies
except Exception as e:
   print ('Error accesing the database')
   print(e)

# pprint(collection)
# print ("\nCollections available")
# pprint(db.list_collection_names())

def find_recepie_db(a_title):
    found = False
    mysearch = collection.find_one({'title':a_title})
    # return error if try to find len
    if str(type(mysearch)) != "<class 'NoneType'>" :
        # print('Mysearch: ',a_title," >> ", type(mysearch))
        # print('Mysearch: ',len(mysearch),mysearch)
        found = True
    return found


# Main
if __name__ == '__main__':
    #
    parsed_topic_name = 'parsed_recipes'
    # Notify if a recipe has more than 200 calories
    calories_threshold = 150

    consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=[KAFKA_HOST], api_version=(0, 10), 
                             consumer_timeout_ms=3000)

    output_list=[]
    for msg in consumer:
        record = json.loads(msg.value)
        calories = int(record['calories'])
        title = record['title']
        # print("Reading recipie for ", title, " (calories=",calories,")" )
        if len(title) >= 5 and calories < calories_threshold:
            print('Alert: {} calories count is {}'.format(title, calories))
            # print(record)
            # Any recepie title should be longer than 5 characters
            if len(title) >= 5 and find_recepie_db(title) == False:
                postid = collection.insert_one(record).inserted_id
                print("\ninserted {} into collection (id={}) ".format(title, postid))
                # print("inserted id: ", postid)
            else:
                print(title, " skipped or already existed") 


    # write file to send in email alert
    with open(output_file, "w") as myfile:
        for rec in output_list:
            myfile.write(rec)

    # sends email
    send_alert(output_file)

    if consumer is not None:
        consumer.close()

