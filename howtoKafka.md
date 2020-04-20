# How to run a Kafka server 
The following steps describe how to run the Kafka/Zookeeper server for this example. Notice that for
production environment the server need configuration that is more complex and secure.

Notes on this example:
* Kafka runs on the local computer (NOT in Docker)
* The configuration chosen is basic and requires adjustment for production 


##### STEP 1. Open 3 terminals (iTerm)
For this example you will require 3 terminals open.  One for each app:  Zookeeper, Kafka, and interactive shell

##### STEP 2. Start Kafka Zookeper
In the folder where you downloaded Kafka (e.g. /Users/john/Downloads/kafka_2.11-2.1.1) do the following:

- Edit the file ``kafka_2.11-2.1.1/config/server.properties`` and update the value of `listener` to listeners=PLAINTEXT://localhost:9092
- Start Zookeeper


```shell
# Edit Zookeepr configuration
$ vi kafka_2.11-2.1.1/config/server.properties

# starting Zookeper
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

# to stop Zookeeper press CTRL-C

```

##### STEP 3. Initiate the Kafka Server
On the same directory where Kakfa was downloaded do the following..

```shell
# Starting Kafka server
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

# To stop presione CTRL-C

```

##### STEP 4. Verify access - Send message to Kafka (as Producer)
Using a simple program we can generate events and send them to Kafka using the topic ``sample``. Steps:


```shell
$ python example-producer.py

sending  message-2  =  Bienvenido
sending  message-3  =  a Kafka
sending  message-4  =  una aventura
sending  message-5  =  en el manejo
sending  message-6  =  de eventos

```

##### STEP 5. Verify access - Reading messages from Kafka (as Consumer)
The following step verifies that we can read messages from the Kafka topic ``sample``. Notice that the our connection
to Kafka is always looking to retrieve messages from the beginning or as ealy as possible (opcion `auto_offset_reset='earliest'`).

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

