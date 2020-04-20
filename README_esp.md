# Aprendiendo conceptos basicos de Docker Containers, Kafka, y MongoDB utilizando Python (pymongo / kafka-python)
En este ejemplo he tomado la idea del ejemplo en Kafka desarrollado por  [Anan Sidiki](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05), 
 adicionando al ejercicio otros componentes tales como MondoDB, y Doker-izacion de todos los layers.

 ** 🇺🇸Back to [English Version ](README.md)**

## El problema
Debemos leer las recetas de "recipies.com", si la receta tiene menos de 200 calorias, vamos a 
generar un alerta y vamos a guardar la receta en nuestro repositorio en MongoDB.

<diagrama generado utilizando plantuml for Gitlab>


```plantuml

skinparam Shadowing false


Recepies.com <- PythonScraper: Lee las recetas
PythonScraper -> Kafka: Envia recetas a topic: RAW 
PythonParser o--> Kafka : Lee recetas de topic: RAW
PythonParser -> PythonParser: Parse en Json 
Kafka <- PythonParser: Envia recectas topic: PARSED
Kafka <- AlertService: Lee recetas topic: PARSED
AlertService -> AlertService: si la condicion aplica

box "Docker Container" #LightGray
database MongoDB #green
AlertService -[#green]-> MongoDB: Guarda recetas en JSON DB-collection
end box

actor Bob #blue
AlertService -[#0000FF]> Bob: envia alertas 

'!include ../../plantuml-styles/ae-copyright-footer.txt
```
### Agradecimiento
Quiero agradecer a todos aquellos que han publicado documentacion en Gitlab, Medium, TowarsDataScience, y otros canales. Gracias a ellos pude crear este 
ejemplo ilustrando los varios componentes del stack technico.

Specialmente gracias a:
* [JSON The Python Way](https://medium.com/python-pandemonium/json-the-python-way-91aac95d4041)
* [Getting Started with Apache Kafka in Python](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05)
* [50 Code Examples from the Web for Kafka ()](https://www.programcreek.com/python/example/98440/kafka.KafkaConsumer)

### Pre-requisitos
La siguiente lista de software necesita ser installada para este ejemplo:
* Docker : docker.com
* Kafka : I used https://github.com/wurstmeister/kafka-docker
* MongoDB : I run on Docker Container https://hub.docker.com/_/mongo
* python-kafka : pip3 install 
* BeautifulSoup4 : pip3 install 
* pymongo : pip3 install


### Iniciando la jornada
Assumiendo que todos los Pre-requisitos 👆han sido installados, lo primero que debemos hacer es validar que los componentes por separado estan funcionando.
La siguiente seccion describe paso a paso cada uno de los componente, uniendo la solucion al final.  

Para referencia, aqui pueden ver la [architectura](howtodockerkafka_esp.md) de la solucion final 

#### Construyendo nuestro ejemplo
debemos hacer es validar que los componentes por separado estan funcionando (Kafka, Zookeeper, MongoDB)

Pasos: 

1. [MongoDB en docker](howtoMongoDB_esp.md)
2. [Kafka en sistema local](howtoKafka_esp.md)

En este momento ya tenemos gran parte de los components corriendo y validados. Los siguientes es conectarlos con un ejemplo demo:

3. [Ejemplo interactivo de Kafka a MongoDb usando Python](fromKafkatoMongo_esp.md)
4. [Creando el primer programa Producer/Consumer](firstexample_esp.md)
5. En este momento podemos correr el siguiente script para verificar que todas las pieces estan funcionando juntas.  Pasos:
* a) abrir dos terminales en shell.  Asegurese que los servidores no estan corriendo (de los pasos anteriores, si ya los inicio, salte al paso (c) ).
* b) en una terminal ejecute `./rundemo.sh servers`.  Espere a que los servidores inicien.
* c) en otra terminal ejecute `./rundemo.sh clients`. Este script correra los mismos test que usted ejecuto individualmente
* d) en la misma terminal ejecute ./rundemo.sh apps.  Este script correra los apps del paso #6 (abajo)



Ya que tenemos todas las partes del problema resueltas, creemos nuestro ejemplo final:

5. [Ejemplo Final - Todos los componentes](finalexample_esp.md)

#### Conclusion
En este ejemplo hemos visto una aplicacion completa (punta-a-punta) donde desarrollamos componentes que encadenan funcionalidad de Kafka - MongoDB - Docker - conectado con Python

#### Llevandolo mas lejos -  Corriendo todo en Docker

El siguiente paso es mover Kafka a Docker Containers de tal manera 
que Mongo/Kafka corren en docker, mientras el codigo ejemplo en el
computador local:

6. [Corriendo Kafka en Docker](howtodockerkafka_esp.md)
 

