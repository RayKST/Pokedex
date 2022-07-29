import requests
import json


for i in range(1, 152):
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
    responseJson = res.json()
    pokeName = responseJson["name"]

    with open(f'pokeinfo/pokemons/{i}-{pokeName}.json', 'w') as data_file:
        json.dump(responseJson, data_file, indent=4)