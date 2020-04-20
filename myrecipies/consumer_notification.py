# https://github.com/kadnan/Calories-Alert-Kafka/blob/master/consumer-notification.py
# Reading from Kafka
# if a recipie is less than a given number of calories then an alert is created

# Si una receta es publicada con menos de 150 calorias entonces una alerta es generada

import json
from time import sleep
import os
from kafka import KafkaConsumer

# Read environment variables
try:
    KAFKA_HOST=os.getenv('KAFKA_HOST','localhost:9092')
except KeyError:
    print ("please set the env. variable for KAFKA_HOST")

output_file="alert.txt"

print ("using KAFKA_HOST = ",KAFKA_HOST)

# main
if __name__ == '__main__':
    parsed_topic_name = 'parsed_recipes'
    # Notify if a recipe has more than threshold calories
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
        if calories < calories_threshold:
            print('Alert: {} calories count is {}'.format(title, calories))
            print(record)
            output_list.append(record)
            # send_notification(msg)
        sleep(3)

    with open(output_file, "w") as myfile:
        for rec in output_list:
            myfile.write(rec)

    if consumer is not None:
        consumer.close()

