import requests

url = "https://api.pokemonbattle.ru/v2/pokemons"
headers = {
    "Content-Type": "application/json",
   "trainer_token": "786a739e39a32cb942a012c0eac72912" 
}
body = {
    "name": "тимоша",
    "photo_id": 11
}
response = requests.post(url, headers=headers, json=body)
print(response.status_code)
print(response.json())

# получить ID покемона из ответа
pokemon_id = response.json()['id']

# изменение имени покемона
url = "https://api.pokemonbattle.ru/v2/pokemons"

headers = {
    "Content-Type": "application/json",
    "trainer_token": "786a739e39a32cb942a012c0eac72912"
}

body = {
    "pokemon_id": pokemon_id,
    "name": "Пика",
    "photo_id": 11
}

update_response = requests.put(url, headers=headers, json=body)
print("Обновление имени:", update_response.status_code)
print(update_response.json())

# третий запрос — поймать покемона в покебол
url = "https://api.pokemonbattle.ru/v2/trainers/add_pokeball"

headers = {
    "Content-Type": "application/json",
    "trainer_token": "786a739e39a32cb942a012c0eac72912"
}

body = {
    "pokemon_id": pokemon_id  # тот же, что мы создавали в первом запросе
}

catch_response = requests.post(url, headers=headers, json=body)
print("Поймать в покебол:", catch_response.status_code)
print(catch_response.json())

