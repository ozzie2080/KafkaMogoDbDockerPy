# COMPLETE EXAMPLE  
Ok, now we are ready to integrate and connect all the various pieces that we creaed so far.


#### STEP 1. Retrieve recipies from URL and publishing them in Kafka
This commandline executes the program `producer_raw_recipies.py`, f you use the KafkaTool you can see
that a new topic was created (named raw_recipies), and contains ten (10) messages to start:


```shell
# step 1. Retieving recipies and publishing to Kafka

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


#### STEP 2. Read recipies from Kafka, remove HTML formatting, encode them, and send them back to Kafka 

In this second program, we read recipies from the topic `raw_recipies`, then we convert them to a record with JSON format:

{'title': title, 'submitter': submit_by, 'description': description, 'calories': calories,
               'ingredients': ingredients}

Finally, we send the recipies to a new Kafka topic `parsed_recepies`. For this, on the commandline, 
run the program: `producer_consumer_parse_recipes.py` 

```shell
# Reads, Cleans, Encodes, and send recipies to Kafka
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


#### STEP 3. Sends email notification if the new recipie is published
This program reads the Kafka topic `consumer_notification` and prints a message if any of the 
recipies is les than 150 calories..

Run the program: `consumer_notification.py`:

```shell
# >> Reads from Kafka parsed recipies and creates a file to alert for those < calories

$ python consumer_notification.py

Alert: Roasted Beet Salad  calories count is 66
{'title': 'Roasted Beet Salad ', 'submitter': 'JP4012K', 'description': 'Roasted beets with balsamic vinegar dressing.', 'calories': '66', 'ingredients': [{'step': '6 medium beets, trimmed and scrubbed'}, {'step': '2 tablespoons aged balsamic vinegar'}, {'step': '2 teaspoons real maple syrup'}, {'step': 'salt and ground black pepper to taste'}]}
Alert: Taco Slaw calories count is 27
{'title': 'Taco Slaw', 'submitter': 'mixingmedias', 'description': 'The local taco truck serves their chicken tacos with cabbage, cilantro and lime.  This is my attempt to recreate their taco toppings.', 'calories': '27', 'ingredients': [{'step': '1/2 small head cabbage, chopped'}, {'step': '1 jalapeno pepper, seeded and minced'}, {'step': '1/2 red onion, minced'}, {'step': '1 carrot, chopped'}, {'step': '1 tablespoon chopped fresh cilantro'}, {'step': '1 lime, juiced'}]}
Alert: - calories count is 0
{'title': '-', 'submitter': '-', 'description': '-', 'calories': 0, 'ingredients': []}
Alert: Mediterranean Greek Salad calories count is 131
{'title': 'Mediterranean Greek Salad', 'submitter': 'Heather', 'description': 'This is a great salad to take to a barbeque. All ingredients are approximate, so add more or less of any ingredient depending on your own taste.', 'calories': '131', 'ingredients': [{'step': '3 cucumbers, seeded and sliced'}, {'step': '1 1/2 cups crumbled feta cheese'}, {'step': '1 cup black olives, pitted and sliced'}, {'step': '3 cups diced roma tomatoes'}, {'step': '1/3 cup diced oil packed sun-dried tomatoes, drained, oil reserved'}, {'step': '1/2 red onion, sliced'}]}

# verify that the file contains the records to be send
$ cat alert.txt

```


#### STEP 4. Saves recipies in a collection on MongoDB  (Really it is a replacement for STEP 3)
Up to this point we receive alerts if new recipies are added.  
The next program is very similar to the one on STEP 3, with the addition for reading / writing to MongoDB

If you need to initiate MongoDb remember the command  `docker run -d -p 27017:27017 -v data:/data/db mongo`, and
the following command for testing the email portion of the example `python -m smtpd -c DebuggingServer -n localhost:1025`


Steps:

```shell
# >> Start a server for SMTP to run this step.  On a different terminal execute:
python -m smtpd -c DebuggingServer -n localhost:1025

# >> Make sure MongoDB container is running 'docker ps'
$ python consumer_save.py

Alert: Roasted Beet Salad  calories count is 66
Roasted Beet Salad   skipped or already existed
Alert: Taco Slaw calories count is 27
Taco Slaw  skipped or already existed
Alert: Mediterranean Greek Salad calories count is 131
Mediterranean Greek Salad  skipped or already existed

```

#### STEP 5. Read recipies from MongoDB

The last part of our exercise is to read the recipies back. For this we are using a very simple program (`dbread_recepies.py`)
that prints the titles, author, and calories of the recipies being saved.

Steps: 

```shell

$ python dbread_recepies.py

Mediterranean Greek Salad     		 Heather	 131
Taco Slaw                     		 mixingmedias	 27
Roasted Beet Salad            		 JP4012K	 66
Roasted Beet Salad            		 JP4012K	 66

```


