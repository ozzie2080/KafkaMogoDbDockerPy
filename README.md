# Learning basic concepts on Docker Containers, Kafka event streaming, and MongoDB using Python (pymong / kafka-python)
In this example we have taken the basic idea posted by [Anan Sidiki](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05), 
 adding to the example other components such as MongoDB, and Docker to run all the various coponents of the solution.

*** 📚🇪🇸Tambien lo puedes leer en [Español aqui](README_esp.md) ***

## Problem to Solve
We need to read recipies from "recipies.com", if the recepies are less than 200 calories, we will generate
an alert, and then will save the recepie in our MongoDB repository

Our design:


```plantuml

skinparam Shadowing false

participant Recepies.com

participant raw_recipies.py as PythonScraper <<PythonScraper>>
participant parse_recipies.py as PythonParser <<PythonParser>>
database Kafka
participant consumer_save.py as AlertService <<AlertService>>

Recepies.com <- PythonScraper: 1. read recipies
PythonScraper -> Kafka: 2. send recipies a topic: RAW
PythonParser o--> Kafka : read recipies from topic: RAW
PythonParser -> PythonParser: Parse in Json 

Kafka <- PythonParser: send recipies to topic: PARSED
Kafka <- AlertService: read recipies from topic: PARSED
AlertService -> AlertService: if condition applies\nadds to file

activate AlertService 
 box "Docker Container" #LightGray
  database MongoDB #green
  AlertService -[#green]-> MongoDB: Save recipies in JSON DB-collection
 end box

 actor Bob #blue
 AlertService -[#0000FF]> Bob: send alerts (email)

deactivate

'!include ../../plantuml-styles/ae-copyright-footer.txt
```
### Acknowledgement
I would like to thank those who published documentation on Gitlab, Medium, TowarsDataScience, and other channels. Thanks to them, I a was able to create
this example demonstrating all the various components in the technical stack.

Specially thanks to:
* [JSON The Python Way](https://medium.com/python-pandemonium/json-the-python-way-91aac95d4041)
* [Getting Started with Apache Kafka in Python](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05)
* [50 Code Examples from the Web for Kafka ()](https://www.programcreek.com/python/example/98440/kafka.KafkaConsumer)

### Prerequisites
The following list of software needs to be install for this example:

* Docker : docker.com
* Kafka : I used https://github.com/wurstmeister/kafka-docker
* MongoDB : I run on Docker Container https://hub.docker.com/_/mongo
* python-kafka : pip3 install 
* BeautifulSoup4 : pip3 install 
* pymongo : pip3 install


### Initiating the journey
Assuming that all the prerequisites have been met 👆, the first thing that we need to do is to verify each component individually
to understand how it works.  The next section describes step-by-step each of the components and how they come togethe in the final solution.

For reference, you can see the final solution here:  [Architecture](howtodockerkafka.md) 

#### Building our solution
Let us validate our components individually: Kafka, Zookeeper, MongoDB

Steps: 

1. [MongoDB on docker](howtoMongoDB.md)
2. [Kafka on local system](howtoKafka.md)

At this point we have our main components workring and validated. Next steps, connecting them as part of the solution:

3. [Interactive example with Kafka and MongoDb using Python](fromKafkatoMongo.md)
4. [Creating the first Kafka Producer/Consumer program](firstexample.md)

5. At this point you should be able to run the following **script to verify all the pieces are working together**. Steps:
* a) open to terminals on shell.  Make sure that the servers are not running. If they are already started (from previous steps, if they are running please go directly to step (c) ) 
* b) on one terminal run `./rundemo.sh servers`.   Wait for the servers to start.
* c) on the other terminal run `./rundemo.sh clients`.  This will run the same scripts that you ran individually.
* d) on the same terminal run `./rundemo.sh apps`.  This will run the myrecipies apps from step #6 (below)

**Now we have the main logic and pieces in place, let's build the final example:**

6. [Final Solution - All components together](finalexample.md)

### Conclusion
In this example we have seen an complete application end-to-end where we connect functionality from Kafka - MongoDB - Docker - using Python

### Taking it to the next level - Everything in Docker
The next level is to move Kafka to a docker container such that Mongo + Kafka are running in containers.  And our code will run on the local
computer or another container.

6. [Running Kafka Docker](howtodockerkafka.md)
 

