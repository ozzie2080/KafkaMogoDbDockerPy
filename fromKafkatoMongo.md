# Example reading from Kafka and Saving a collection on MongoDB

```plantuml

title Basic data flow between MongoDB and Kafka

skinparam Shadowing false

actor YouPython #blue
YouPython -> Kafka: send messages
database MongoDB #green
Kafka <-[#green]-> MongoDB: Save messages on JSON DB-collection

```


**Below are the transformation that we need to apply to a JSON formatted message**


```plantuml

title Data Transformations 

skinparam Shadowing true
skinparam roundcorner 20


mensaje_json -> producer: converts json.dump()
producer -> producer: converts bytes()
producer -> kafka: send message 
kafka -> kafka: adds message to the queue
kafka <-[#green]o consumer: reads messages
consumer -> consumer: decodes bytes.decode()
consumer -> consumer: converts message json.load()
database MongoDB #green
consumer -[#green]> MongoDB: send colleccion insert()

```

Basic steps
* Connect to the dabase
* Connect to Kafka
* Create messages in Json format
* Send messages to Kafka
* retrieve message from Kafka
* send messages to Mongo

These are the steps using Python CLI:

```python

# In python shell
$ python
>>>
# ########
# FIRST MONGODB
# ########
>>> Open coneccion a Mongo
>>> from pymongo import MongoClient
>>> from pprint import pprint
>>> client = MongoClient('mongodb://localhost:27017/')
>>> db = client.mydb
>>> pprint(db.list_collection_names())
# resultado
['recepies', 'cities', 'post', 'cars']

# select cities from our collection
>>> collection = db.cities
>>> for a in collection.find():
    ... print(a)
# Resultado
{'_id': ObjectId('5e3f3c3e6a2700f01d5ec888'), 'name': 'New York', 'country': 'USA'}
{'_id': ObjectId('5e3f3c3e6a2700f01d5ec889'), 'name': 'Paris', 'country': 'France'}
{'_id': ObjectId('5e3f50f2b25a3628640a1e4b'), 'name': 'Seattle', 'country': 'USA'}
{'_id': ObjectId('5e3f5353b25a3628640a1e4c'), 'country': 'Canada', 'name': 'Vancouver'}
{'_id': ObjectId('5e3f5353b25a3628640a1e4d'), 'country': 'Mexico', 'name': 'Mexicali'}
{'_id': ObjectId('5e3f53eeb25a3628640a1e4e'), 'country': 'Canada', 'name': 'Quebec', 'languages': ['English', 'French']}
{'_id': ObjectId('5e45e8b09421f82f87eac0e8'), 'name': 'Los Angeles', 'country': 'USA'}
{'_id': ObjectId('5e51c9185bc8be528d159995'), 'name': 'Toronto', 'country': 'Canada'}
{'_id': ObjectId('5e52f75a95e220e59383798c'), 'name': 'Madrid', 'country': 'Spain'}
{'_id': ObjectId('5e52fe2495e220e59383798d'), 'name': 'Madrid', 'country': 'Spain', 'languages': ['Spanish', 'Catalan']}
{'_id': ObjectId('5e5db55681c411b918c858a9'), 'name': 'Lima', 'country': 'Peru'}

# ########
# SECOND KAFKA
# ########
# >>> Producer: Takes a message, conversts to json / bytes, and send to Kafka
>>> import json
>>> from kafka import KafkaProducer
>>> producer = KafkaProducer(bootstrap_servers='localhost:9092')
>>> acity = {'name': 'Lima', 'country': 'Peru'}
# convirtiendo a Json
>>> jsoncity = json.dumps(acity)
>>> citybytes = bytes(jsoncity, encoding='utf-8')
>>> citybytes
b'{"name": "Lima", "country": "Peru"}'

>>> producer.send('oztest1', value=citybytes)
<kafka.producer.future.FutureRecordMetadata object at 0x102c1b160>

# >>> Consumer: Reads messages from Kafka, and Decodes 
# >>> This will print all the messages from Kafka
>>> from kafka import KafkaConsumer
>>> consumer = KafkaConsumer('oztest1', bootstrap_servers=['localhost:9092'], api_version=(0, 10), auto_offset_reset='earliest',consumer_timeout_ms=1000)
>>> for msg in consumer:
...    print(msg)
...

ConsumerRecord(topic='oztest1', partition=3, offset=0, timestamp=1585103973292, timestamp_type=0, key=b'message-1004', value=b'una aventura', headers=[], checksum=2442140435, serialized_key_size=12, serialized_value_size=12, serialized_header_size=-1)
ConsumerRecord(topic='oztest1', partition=3, offset=1, timestamp=1585103974330, timestamp_type=0, key=b'message-1005', value=b'en el manejo', headers=[], checksum=4053552911, serialized_key_size=12, serialized_value_size=12, serialized_header_size=-1)
ConsumerRecord(topic='oztest1', partition=3, offset=2, timestamp=1585106454674, timestamp_type=0, key=None, value=b'{"name": "Lima", "country": "Peru"}', headers=[], checksum=2307476889, serialized_key_size=-1, serialized_value_size=35, serialized_header_size=-1)
ConsumerRecord(topic='oztest1', partition=1, offset=0, timestamp=1585103971232, timestamp_type=0, key=b'message-1002', value=b'Bienvenido', headers=[], checksum=2170847914, serialized_key_size=12, serialized_value_size=10, serialized_header_size=-1)
ConsumerRecord(topic='oztest1', partition=1, offset=1, timestamp=1585103972253, timestamp_type=0, key=b'message-1003', value=b'a Kafka', headers=[], checksum=3311813990, serialized_key_size=12, serialized_value_size=7, serialized_header_size=-1)
ConsumerRecord(topic='oztest1', partition=0, offset=0, timestamp=1585103975358, timestamp_type=0, key=b'message-1006', value=b'de eventos', headers=[], checksum=2371263753, serialized_key_size=12, serialized_value_size=10, serialized_header_size=-1)

# >> checking the type of the last message received "msg"
>>> type(msg)
 <class kafka.consumer.fetcher.ConsumerRecord >

# Cheking some values inside the message msg
>>> print (msg.value, msg.key, msg.offset, msg.timestamp)
b'de eventos' b'message-1006' 0 1585103975358

>>> print (msg.value)
b'de eventos'
>>> print (bytes.decode(msg.value))
de eventos

# ########
# BACK TO MONGODB
# ########

# >>> MongoDB: Save the collection on the DB 
# >>> Insert messages into MongoDB (as collection).  Assuming that the data received is
#     in byte / JSON.  (remember, we add this to illustrate our example)

# {dicitonary} -> a JSON json.dumps() -> a BYTES bytes(variable, encoding='utf-8')
#  BYTES -> bytes.decode() -> json.loads() -> {dictionary}

>>> newcity={"name": "Sao Paolo", "country":"Brazil"}

>>> jsonnewcity=json.dumps(newcity)
>>> jsonnewcity
'{"name": "Sao Paolo", "country": "Brazil"}'
>>> type(jsonnewcity)
<class 'str'>

>>> bytesnewcity=bytes(jsonnewcity, encoding='utf-8')
>>> bytesnewcity
b'{"name": "Sao Paolo", "country": "Brazil"}'
>>> type(bytesnewcity)
<class 'bytes'>

# >> Decodes the byte format for the dictionary
>>> anothercity=bytes.decode(bytesnewcity)
>>> anothercity
 '{"name": "Sao Paolo", "country": "Brazil"}'

>>> decodecity=bytes.decode(bytesnewcity)
>>> type(decodecity)
 <class 'str'>

>>> loadcity=json.loads(decodecity)
>>> loadcity
{'name': 'Sao Paolo', 'country': 'Brazil'}

# >> This is the object that we have to insert into MongoDB
>>> type(loadcity)
<class 'dict'>

# view details on our "collection"
>>> collection
Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'mydb'), 'cities')

>>> collection.insert_one(loadcity)
<pymongo.results.InsertOneResult object at 0x102c15ac8>

>>> for a in collection.find():
...    print(a)
...
{'_id': ObjectId('5e3f3c3e6a2700f01d5ec888'), 'name': 'New York', 'country': 'USA'}
{'_id': ObjectId('5e3f3c3e6a2700f01d5ec889'), 'name': 'Paris', 'country': 'France'}
{'_id': ObjectId('5e3f50f2b25a3628640a1e4b'), 'name': 'Seattle', 'country': 'USA'}
{'_id': ObjectId('5e3f5353b25a3628640a1e4c'), 'country': 'Canada', 'name': 'Vancouver'}
{'_id': ObjectId('5e3f5353b25a3628640a1e4d'), 'country': 'Mexico', 'name': 'Mexicali'}
{'_id': ObjectId('5e3f53eeb25a3628640a1e4e'), 'country': 'Canada', 'name': 'Quebec', 'languages': ['English', 'French']}
{'_id': ObjectId('5e45e8b09421f82f87eac0e8'), 'name': 'Los Angeles', 'country': 'USA'}
{'_id': ObjectId('5e51c9185bc8be528d159995'), 'name': 'Toronto', 'country': 'Canada'}
{'_id': ObjectId('5e52f75a95e220e59383798c'), 'name': 'Madrid', 'country': 'Spain'}
{'_id': ObjectId('5e52fe2495e220e59383798d'), 'name': 'Madrid', 'country': 'Spain', 'languages': ['Spanish', 'Catalan']}
{'_id': ObjectId('5e5db55681c411b918c858a9'), 'name': 'Lima', 'country': 'Peru'}
{'_id': ObjectId('5e7ad6bf688bf160d925124c'), 'name': 'Sao Paolo', 'country': 'Brazil'}

# >> Searching for a single specific value  
>>> for a in collection.find({'country':'Brazil'}):
...    print(a)
...

{'_id': ObjectId('5e7ad6bf688bf160d925124c'), 'name': 'Sao Paolo', 'country': 'Brazil'}


```
