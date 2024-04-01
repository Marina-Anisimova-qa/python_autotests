import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : 'ТОКЕН'}


body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body) #ответ на запрос создание покемона

print(response.text)

data = response.json() # присваиваю переменную равной ответу

id = data['id'] # присваиваю переменную 

body = {
    "pokemon_id": id,
    "name": "generate",
    "photo": "generate"
}

response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body) # ответ на запрос изменения имени покемона

print(response.text)

body = {
    "pokemon_id": id
}

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body) # ответ на запрос поймать покемона в покебол

print(response.text)
