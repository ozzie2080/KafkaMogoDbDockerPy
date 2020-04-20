# Example to test connectivity to Kafka
# Author: Ozzie Farfan

from kafka import KafkaProducer
import time

mykafkaserver="localhost:9092"
mytopic="ozsample1"
mytopic="oztest1"

try:
   producer = KafkaProducer(bootstrap_servers=mykafkaserver)
   # producer = KafkaProducer(bootstrap_servers='10.230.89.218:9092')
except Exception as e:
   print ("Error conectandose a Kafka")
   print (e)

# producer.send('sample', b'Mi Primer Kafka Producer') 

mymessage = ['Bienvenido','a Kafka','una aventura','en el manejo','de eventos']

key=1001
for m in mymessage:
    key = key + 1 
    mkey = 'message-'+str(key)
    print ("sending ",mkey," = ",m)
    # message encoded to ensure valid unicode as expected by Kafka
    key_bytes = bytes(mkey, encoding='utf-8')
    value_bytes = bytes(m, encoding='utf-8')
    producer.send(mytopic, key=key_bytes, value=value_bytes)
    producer.flush()
    # delay introduced just for illustration purposes (not needed by Kakfa)
    time.sleep(1)

