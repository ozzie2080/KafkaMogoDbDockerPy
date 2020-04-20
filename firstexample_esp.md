## Nuestro primer ejemplo Enviando/Recibiendo mensajes de Kafka desde un programa

En el ejercicio anterior vimos todos los pasos requeridos para enviar y recibir 
mensajes de Kafka.

Los siguientes ejemplos ilustran los mismos conceptos pero ya como parte de un 
programa Python.  Utilice los programas llamados: `example-producer.py` y `example-consumer.py`.

Pasos:

```shell
# Asumiendo que Zookeeper y Kafka estan corriendo
# Enviando mensajes
$ python example-producer.py

sending  message-1002  =  Bienvenido
sending  message-1003  =  a Kafka
sending  message-1004  =  una aventura
sending  message-1005  =  en el manejo
sending  message-1006  =  de eventos

# Si utiliza una herramienta como kafka-tool (kafkatool.com) puede ver los mensajes
# en la cola de Kafka

# Leyendo todos los mensajes
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
