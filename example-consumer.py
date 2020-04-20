# Example to test connectivity to Kafka
# Author: Ozzie Farfan

from kafka import KafkaConsumer

# consumer = KafkaConsumer('sample')
parsed_topic_name='oztest1'

try:
   consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest',
                  bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=5000)
except Exception as e:
    print ("Error conectandose a Kafka")
    print (e)

# Display message, and extracts the content
for message in consumer:
    print(message)
    msg = bytes.decode(message.value)
    # msglist = msg.split(",")
    # print(msglist)
    print("content: ", msg)


