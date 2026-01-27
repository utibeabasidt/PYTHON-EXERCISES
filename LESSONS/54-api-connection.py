'''How to connect to an API using python'''
'''first of all install requests via pip becuase it is not a built-in python module'''

import requests 

raw_url = 'https://pokeapi.co/api/v2/' # primary url

def get_pokemon_info(name):
  final_url = f'{raw_url}/pokemon/{name}' # secondary url, containing the attributes
  response = requests.get(final_url) # getting the reponse value whenever the the url is executed
  if response.status_code == 200:
    print('Get response is successful. Data retrieved.') # if the response status code is okay, then data is retrived
    pokemon_data = response.json() # get the api response data (json by default) and convert it to a python dictionary
    return pokemon_data # return the dictionary data to be used
  else:
    print(f'Failed response: {response.status_code}') # return the error message

pokemon_name = 'Typhlosion'
pokemon_info = get_pokemon_info(pokemon_name) # gets the dictionary after passing the argument for fetching the api

# if the dictionary truly exists, then access values from the key
if pokemon_info:
  print(f'Name: {pokemon_info.get('name')}')  # name
  print(f'Id: {pokemon_info.get('id')}') # id
  print(f'Height: {pokemon_info.get('height')}') # height
  print(f'Weight: {pokemon_info.get('weight')}') # weight


'''STEPS (inside a function):
  Get the base and final url
  Using the requests.get() method, get the response value of the the reequest
  If the response value is okay, get the api json data and convert it to a dictionary using the json() method and save it in a variable
  Return that variable to be used outside the function.

  (outside the function):
  You can save the return value to a variable and then access each of the dictionary keys to get the data
'''