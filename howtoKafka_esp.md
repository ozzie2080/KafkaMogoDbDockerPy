# Como correr el servidor de Kafka
Los siguientes pasos describen como correr el servidor de Kafka/Zookeper para el ejemplo. Note que para 
ambientes en produccion el servidor necesita configuraciones mas complejas y seguras.

Notas de este ejemplo:
* Kafka corre en el computador local (no en Docker)
* La configuracion utilizada es basica y requiere mas ajustes para produccion

##### 1. Abrir 3 terminales (iTerm)
Para este ejemplo se requiere tener 3 terminales abiertas: Zookeeper, Kafka, y terminal interactiva

##### 2. Iniciar Kafka Zookeper
En el directorio donde extrajo Kafka..(e.g. /Users/john/Downloads/kafka_2.11-2.1.1) ejecute los siguientes pasos:
- Edite el archivo kafka_2.11-2.1.1/config/server.properties y actualize el valor del `listener` a 
listeners=PLAINTEXT://localhost:9092
- inicie Zookeeper


```shell
# iniciando Zookeper
$ bin/zookeeper-server-start.sh config/zookeeper.properties

# output
[2020-02-24 21:05:00,080] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2020-02-24 21:05:00,088] INFO autopurge.snapRetainCount set to 3 (org.apache.zookeeper.server.DatadirCleanupManager)
[2020-02-24 21:05:00,097] INFO autopurge.purgeInterval set to 0 (org.apache.zookeeper.server.DatadirCleanupManager)
[2020-02-24 21:05:00,097] INFO Purge task is not scheduled. (org.apache.zookeeper.server.DatadirCleanupManager)
< extra texto removido >
[2020-02-24 21:05:00,176] INFO minSessionTimeout set to -1 (org.apache.zookeeper.server.ZooKeeperServer)
[2020-02-24 21:05:00,176] INFO maxSessionTimeout set to -1 (org.apache.zookeeper.server.ZooKeeperServer)
[2020-02-24 21:05:00,207] INFO Using org.apache.zookeeper.server.NIOServerCnxnFactory as server connection factory (org.apache.zookeeper.server.ServerCnxnFactory)
[2020-02-24 21:05:00,233] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)

# Para parar Zookeeper presione CTRL-C

```

##### 3. Iniciar Kafka Server
En el directorio donde extrajo Kafka..(e.g. /Users/john/Downloads/kafka_2.11-2.1.1) ejecute los siguientes pasos:


```shell
$ bin/kafka-server-start.sh config/server.properties

# output
[2020-02-24 21:09:50,763] INFO Registered kafka:type=kafka.Log4jController MBean (kafka.utils.Log4jControllerRegistration$)
[2020-02-24 21:09:51,273] INFO starting (kafka.server.KafkaServer)
[2020-02-24 21:09:51,274] INFO Connecting to zookeeper on localhost:2181 (kafka.server.KafkaServer)
[2020-02-24 21:09:51,303] INFO [ZooKeeperClient] Initializing a new session to localhost:2181. (kafka.zookeeper.ZooKeeperClient)
[2020-02-24 21:09:51,322] INFO Client environment:zookeeper.version=3.4.13-2d71af4dbe22557fda74f9a9b4309b15a7487f03, built on 06/29/2018 00:39 GMT (org.apache.zookeeper.ZooKeeper)
< extra texto removido >
[2020-02-24 21:09:54,454] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-45 in 0 milliseconds. (kafka.coordinator.group.GroupMetadataManager)
[2020-02-24 21:09:54,454] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-48 in 0 milliseconds. (kafka.coordinator.group.GroupMetadataManager)
[2020-02-24 21:09:54,454] INFO [GroupMetadataManager brokerId=0] Finished loading offsets and group metadata from __consumer_offsets-15 in 0 milliseconds. (kafka.coordinator.group.GroupMetadataManager)

# Para parar Zookeeper presione CTRL-C

```

##### 4. Verficar acceso -  Enviar mensajes a Kafka (Producer)
Utilizando un programa simple como Producer podemos generar mensajes/eventos y enviarlos a Kafka usando el Topico 'sample'.  
Pasos:


```shell
$ python example-producer.py

sending  message-2  =  Bienvenido
sending  message-3  =  a Kafka
sending  message-4  =  una aventura
sending  message-5  =  en el manejo
sending  message-6  =  de eventos

```

##### 5. Verficar acceso -  Leer mensajes de Kafka (Kafka)
El siguiente paso es verificar que podemos leer mensajes de topico 'sample' del servidor Kafka. Note que la linea de 
acceso a Kafka siempre trata de recuperar todos los mensajes (opcion `auto_offset_reset='earliest'`). En este caso
queremos poder correr el programa varias veces sin tener que generar mas mensajes.

Pasos:


```shell
$ python example-consumer.py

python example-consumer.py

ConsumerRecord(topic='sample', partition=0, offset=7, timestamp=1583169443792, timestamp_type=0, key=b'message-secret', value=b'Esto es Kafka-Python', headers=[], checksum=2583553393, serialized_key_size=14, serialized_value_size=20, serialized_header_size=-1)
# content:  Mi Primer Kafka Producer
ConsumerRecord(topic='sample', partition=0, offset=9, timestamp=1583169935353, timestamp_type=0, key=b'message-2', value=b'Bienvenido', headers=[], checksum=190584985, serialized_key_size=9, serialized_value_size=10, serialized_header_size=-1)
# content:  Bienvenido
ConsumerRecord(topic='sample', partition=0, offset=10, timestamp=1583169936416, timestamp_type=0, key=b'message-3', value=b'a Kafka', headers=[], checksum=2146617535, serialized_key_size=9, serialized_value_size=7, serialized_header_size=-1)
# content:  a Kafka
ConsumerRecord(topic='sample', partition=0, offset=11, timestamp=1583169937423, timestamp_type=0, key=b'message-4', value=b'una aventura', headers=[], checksum=3441220622, serialized_key_size=9, serialized_value_size=12, serialized_header_size=-1)
# content:  una aventura
ConsumerRecord(topic='sample', partition=0, offset=12, timestamp=1583169938452, timestamp_type=0, key=b'message-5', value=b'en el manejo', headers=[], checksum=1733888269, serialized_key_size=9, serialized_value_size=12, serialized_header_size=-1)
# content:  en el manejo
ConsumerRecord(topic='sample', partition=0, offset=13, timestamp=1583169939480, timestamp_type=0, key=b'message-6', value=b'de eventos', headers=[], checksum=692001409, serialized_key_size=9, serialized_value_size=10, serialized_header_size=-1)
# content:  de eventos

```

