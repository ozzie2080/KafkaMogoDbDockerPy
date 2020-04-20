## Our First example Sending/Receiving messages from Kafka using Python

In previous session we saw step-by-step how to send/receive messages from Kakfa. 
In this example, we are goig to use the same concepts but now we put them togethe as par of 
a Python program.  Use the two programs:  `example-producer.py` y `example-consumer.py`.

Steps:

```shell
# Assuming Zookeeper and Kafka are still running
# Sending messages - PRODUCER
$ python example-producer.py

sending  message-1002  =  Bienvenido
sending  message-1003  =  a Kafka
sending  message-1004  =  una aventura
sending  message-1005  =  en el manejo
sending  message-1006  =  de eventos

# If you use a tool such as kafka-tool (kafkatool.com) you can see the messages 
# in the kafka queue (plus other details, such as partitions)

# Reading messages - CONSUMER
$ python example-consumer.py

ConsumerRecord(topic='sample', partition=0, offset=0, timestamp=1583601761430, timestamp_type=0, key=b'message-1002', value=b'Bienvenido', headers=[], checksum=4254573388, serialized_key_size=12, serialized_value_size=10, serialized_header_size=-1)
content:  Bienvenido
ConsumerRecord(topic='sample', partition=0, offset=1, timestamp=1583601869183, timestamp_type=0, key=b'message-1002', value=b'Bienvenido', headers=[], checksum=676290806, serialized_key_size=12, serialized_value_size=10, serialized_header_size=-1)
content:  Bienvenido
ConsumerRecord(topic='sample', partition=0, offset=2, timestamp=1583601870243, timestamp_type=0, key=b'message-1003', value=b'a Kafka', headers=[], checksum=4145838620, serialized_key_size=12, serialized_value_size=7, serialized_header_size=-1)
content:  a Kafka
ConsumerRecord(topic='sample', partition=0, offset=3, timestamp=1583601871255, timestamp_type=0, key=b'message-1004', value=b'una aventura', headers=[], checksum=3549716802, serialized_key_size=12, serialized_value_size=12, serialized_header_size=-1)
content:  una aventura
ConsumerRecord(topic='sample', partition=0, offset=4, timestamp=1583601872271, timestamp_type=0, key=b'message-1005', value=b'en el manejo', headers=[], checksum=1767036589, serialized_key_size=12, serialized_value_size=12, serialized_header_size=-1)
content:  en el manejo
ConsumerRecord(topic='sample', partition=0, offset=5, timestamp=1583601873282, timestamp_type=0, key=b'message-1006', value=b'de eventos', headers=[], checksum=569447169, serialized_key_size=12, serialized_value_size=10, serialized_header_size=-1)
content:  de eventos

```
