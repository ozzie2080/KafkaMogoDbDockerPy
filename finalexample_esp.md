# Ejemplo Completo
Bueno, ya estamos listos para conectar todas las partes que hemos creado hasta
ahora.

#### 1. Recolectar las recetas y guardarlas en Kakfa
En la linea de comando ejecute el programa `producer_raw_recipies.py`, si verifica
en Kafka-Tool puede observar que un nuevo topico fue creado (llamado raw_recipies), y 
contiene diez (10) mensajes inicialmente :

```shell
# Paso 1.  Recolectar las recetas y guardarlas en kafka

$ python producer_raw_recipies.py

Accessing list
Processing..https://www.allrecipes.com/recipe/24540/crab-salad-iii/
Processing..https://www.allrecipes.com/recipe/270850/roasted-beet-salad/
Processing..https://www.allrecipes.com/recipe/215030/taco-slaw/
Processing..https://www.allrecipes.com/recipe/254568/all-american-loaded-baked-potato-salad/
Processing..https://www.allrecipes.com/recipe/270199/freekeh-salad-with-tahini-dressing/
Processing..https://www.allrecipes.com/recipe/266401/cucumber-chicken-salad-with-spicy-peanut-dressing/
Processing..https://www.allrecipes.com/recipe/269287/all-kale-caesar/
Processing..https://www.allrecipes.com/recipe/52734/awesome-pasta-salad/
Processing..https://www.allrecipes.com/recipe/14403/mediterranean-greek-salad/
Processing..https://www.allrecipes.com/recipe/14469/jamies-cranberry-spinach-salad/
Processing..https://www.allrecipes.com/recipe/142027/sweet-restaurant-slaw/
Message published successfully.
Message published successfully.
```


#### 2. Leer recetas de Kafka, convertirlas, y enviar de nuevo a Kafka
Este segundo programa lee las recetas que se encuentran en el topico `raw_recipies`, luego las convierte en un registro de formato Json:  

{'title': title, 'submitter': submit_by, 'description': description, 'calories': calories,
               'ingredients': ingredients}

y finalmente, envia las recetas de nuevo a Kafka en un nuevo topico `parsed_recepies`.
En la linea de comando ejecute el programa: `producer_consumer_parse_recipes.py` :


```shell
# Lee, convierte, y envia recetas a Kafka
$ python producer_consumer_parse_recipes.py

Running Consumer..
Publishing records..
Message published successfully.
Message published successfully.
Message published successfully.
Message published successfully.
Message published successfully.
Message published successfully.
Message published successfully.
Message published successfully.
Message published successfully.
Message published successfully.
Message published successfully.

```


#### 3. Recibir notificacion si nuevas recetas son publicadas
Este programa lee la cola de recetas de Kafka e imprime una notificacion si alguna de
las recetas tiene menos de 150 calorias.

Ejecute el programa `producer_consumer_parse_recipes.py`:


```shell
# >> Programa para leer notificaciones de Kafka

$ python consumer_notification.py

Alert: Roasted Beet Salad  calories count is 66
{'title': 'Roasted Beet Salad ', 'submitter': 'JP4012K', 'description': 'Roasted beets with balsamic vinegar dressing.', 'calories': '66', 'ingredients': [{'step': '6 medium beets, trimmed and scrubbed'}, {'step': '2 tablespoons aged balsamic vinegar'}, {'step': '2 teaspoons real maple syrup'}, {'step': 'salt and ground black pepper to taste'}]}
Alert: Taco Slaw calories count is 27
{'title': 'Taco Slaw', 'submitter': 'mixingmedias', 'description': 'The local taco truck serves their chicken tacos with cabbage, cilantro and lime.  This is my attempt to recreate their taco toppings.', 'calories': '27', 'ingredients': [{'step': '1/2 small head cabbage, chopped'}, {'step': '1 jalapeno pepper, seeded and minced'}, {'step': '1/2 red onion, minced'}, {'step': '1 carrot, chopped'}, {'step': '1 tablespoon chopped fresh cilantro'}, {'step': '1 lime, juiced'}]}
Alert: - calories count is 0
{'title': '-', 'submitter': '-', 'description': '-', 'calories': 0, 'ingredients': []}
Alert: Mediterranean Greek Salad calories count is 131
{'title': 'Mediterranean Greek Salad', 'submitter': 'Heather', 'description': 'This is a great salad to take to a barbeque. All ingredients are approximate, so add more or less of any ingredient depending on your own taste.', 'calories': '131', 'ingredients': [{'step': '3 cucumbers, seeded and sliced'}, {'step': '1 1/2 cups crumbled feta cheese'}, {'step': '1 cup black olives, pitted and sliced'}, {'step': '3 cups diced roma tomatoes'}, {'step': '1/3 cup diced oil packed sun-dried tomatoes, drained, oil reserved'}, {'step': '1/2 red onion, sliced'}]}

```


#### 4. Grabar las recetas en MongoDB
Hasta ahora ya tenemos las recetas en Kafka y recibimos alertas si alguna de interes es publicada.

El programa para este paso (`consumer_save.py`) es muy parecido al paso #3, con la 
adicion de codigo para leer y grabar en MongoDB

Si necesita iniciar MongoDB recuerde el comando `docker run -d -p 27017:27017 -v data:/data/db mongo`.

Pasos:


```shell
# >> Asegurese que MongoDB esta corriendo, usando el comando 'docker ps'
$ python consumer_save.py

Alert: Roasted Beet Salad  calories count is 66
Roasted Beet Salad   skipped or already existed
Alert: Taco Slaw calories count is 27
Taco Slaw  skipped or already existed
Alert: Mediterranean Greek Salad calories count is 131
Mediterranean Greek Salad  skipped or already existed

```

#### 5. Leer recetas de MongoDB
La ultima parte de nuestro ejercicio es poder leer las recetas de Mongo.  Para esto vamos
a utilizar un ejemplo sencillo (`dbread_recepies.py`).  El programa lee e imprime los titulos
de todas las recetas que hemos guardado.

Pasos: 


```shell

$ python dbread_recepies.py

Mediterranean Greek Salad     		 Heather	 131
Taco Slaw                     		 mixingmedias	 27
Roasted Beet Salad            		 JP4012K	 66
Roasted Beet Salad            		 JP4012K	 66
```

