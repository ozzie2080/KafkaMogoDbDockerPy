#!/bin/sh
# This script will run all the different components for and end-2-end demo
# please make sure to update the Path to Kafka, etc. below.
# Two modes for running:
#    ./rundemo.sh servers      To start the servers for Mongo / Kafka
#    ./rundemo.sh clients      To run the client testing programs for Mongo and Kafka
#    ./rundemo.sh apps         To run the myrecipies apps

debug="Y"
debug="N"

# KAFKA DOWNLOAD
KAFKA_DIR=~/Downloads/kafka_2.11-2.1.1
# KAFKA DOCKER DOWNLOAD
DOCKER_KAFKA=~/Downloads/Kafka-docker
# MONGO DATA LOCATION
MONGO_DATA=/data/db

# Function to start kafka
start_kafka() 
{ 
	echo "Starting Kafka in $KAFKA_DIR"
	if [ "$debug" == "Y" ]
	then
	   return
	fi

	echo "configuring"
	# replaces the listeners= configuration line with the right entry
	CONFIGFILE=$KAFKA_DIR/config/server.properties
	result=`grep '^listeners=PLAINTEXT:\/\/localhost:9092' ${CONFIGFILE}`
	if [ "$result" == "" ]
	then
		echo "Updating config file ${CONFIGFILE}"
		if [ ! -f ${CONFIGFILE}.ori ]
		then
			cp ${CONFIGFILE} ${CONFIGFILE}.ori
		fi
		sed -e "s/^listeners=.*/listeners=PLAINTEXT:\/\/localhost:9092/" ${CONFIGFILE}.ori> ${CONFIGFILE} 
	fi
	cd $KAFKA_DIR
	echo "${KAFKA_DIR}/bin/zookeeper-server-start.sh config/zookeeper.properties &"
	${KAFKA_DIR}/bin/zookeeper-server-start.sh ${KAFKA_DIR}/config/zookeeper.properties &
	sleep 10
	echo "${KAFKA_DIR}/bin/kafka-server-start.sh config/server.properties &"
	${KAFKA_DIR}/bin/kafka-server-start.sh ${KAFKA_DIR}/config/server.properties &
}


start_kafkadocker()
{
	echo "Starting Kafka docker"
	cd $DOCKER_KAFKA
	CONFIGFILE=$DOCKER_KAFKA/docker-compose-single-broker.yml
	myIP=`ipconfig getifaddr en0`
	if [ ! -f ${CONFIGFILE}.ori ]
	then
		cp ${CONFIGFILE} ${CONFIGFILE}.ori
	fi
	sed -e "s/KAFKA_ADVERTISED_HOST_NAME:.*/KAFKA_ADVERTISED_HOST_NAME: $myIP/" ${CONFIGFILE}.ori > ${CONFIGFILE}
	docker-compose -f docker-compose-single-broker.yml up -d
}


test_kafka()
{
	pcmd="python example-producer.py"
        cmd="python example-consumer.py"
	if [ "$debug" == "N" ]
	then
		echo "Verifying producer.."
		$pcmd
		echo "Verifying consumer.."
		$cmd
	else
		echo $cmd
	fi
}


start_mongodb()
{
	echo "Starting MongoDB container"
	cmd="docker run -d -p 27017:27017 -v data:$MONGO_DATA mongo"
	if [ "$debug" == "N" ]
	then
		$cmd
	else
		echo $cmd
	fi
}


test_mongodb()
{
	echo "Starting MongoDB Test"
	cmd="python test_pymongo.py"
	if [ "$debug" == "N" ]
	then
		$cmd
	else
		echo $cmd
	fi
}


check_process() {
        proc="$1"
	z=`ps -awx | grep -v grep | grep $1`
	if [ "$z" != '' ]; then
		echo "Error: It seems that there is already an instance of $1 running"
		exit
	fi
	return 0
}

test_myrecipies() {
	# reads recipies from myrecipies.com and send them to kafka
	cd myrecipies
	echo "Starting producer_raw_recipies.py.."
	python producer_raw_recipies.py
	# reads recipies from kafka and remove all HTML encoding
	echo "Starting producer_consumer_parse_recipies.py..."
	python producer_consumer_parse_recipies.py
	# read decoded recipies from kafka, if new then save to Mongodb, and sends email 
	# python consumer_notification.py
	echo "Starting consumer_save.py...."
	python consumer_save.py
}


check_docker() {
        proc="$1"
	z=`docker ps | grep -v grep | grep $1`
	if [ "$z" != '' ]; then
		echo "Error: It seems that there is already a Docker instance of $1 running"
		docker ps
		exit
	fi
	return 0
}

# Main function

echo $#
if [ $# == 0 ]
then
	echo "$0 [servers/clients/apps]"
	echo "Remember to start SERVERS and CLIENTS on different shell terminals"
	exit 1
fi

if [ "$1" == "servers" ] 
then
	echo "Starting servers"
	check_docker mongo
	check_process zookeeper
	check_process kafka

	start_mongodb
	# start_kafka
	start_kafkadocker
	exit
fi

if [ "$1" == "clients" ] 
then
	test_mongodb
	test_kafka
	exit
fi

if [ "$1" == "apps" ] 
then
	test_myrecipies
	exit
fi

echo "ERROR: $0 [servers|clients]  Must indicate the mode to start server or test clients"

