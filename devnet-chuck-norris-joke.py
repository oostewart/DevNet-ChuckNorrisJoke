import requests
import json

response = requests.get('https://api.chucknorris.io/jokes/random')

# print(response.text) - remove comment to see json response text

json_object = json.loads(response.text)

joke = json_object['value']

print('Random Chuck Norris Joke: ' + joke)
 
#response.close()
