from htmltojson import *
import requests
from bs4 import BeautifulSoup, NavigableString
import json


with open('src\pokemonstats.json', 'r') as myfile:
    data = myfile.read()

pokemonlist = json.loads(data)



def generate_learnset(pokemon_name):
    response = requests.get(
        f'https://pokemondb.net/pokedex/{pokemon_name}/moves/1')

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find("table")

    for element in table.find_all(string="—"):
        element.string.replace_with("none")

    for element in table.find_all(string="∞"):
        element.string.replace_with("infinite")

    for element in table.find_all(attrs={"data-sort-value": "physical"}):
        element.insert(0, NavigableString("physical"))

    for element in table.find_all(attrs={"data-sort-value": "special"}):
        element.insert(0, NavigableString("special"))

    for element in table.find_all(attrs={"data-sort-value": "status"}):
        element.insert(0, NavigableString("status"))

    with open("learnsets.json", "a") as o:
        o.write('{"' + pokemon_name + '":')
        o.write(html_to_json(table))
        o.write('},')




with open("learnsets.json", "a") as o:
    o.write("[")

for pokemon in pokemonlist:
    pokemon_name = pokemon['name']
    generate_learnset(pokemon_name)

with open("learnsets.json", "a") as o:
    o.write("{" + "}]")