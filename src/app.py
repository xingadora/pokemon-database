from htmltojson import *
import json
import requests
from bs4 import BeautifulSoup, NavigableString


pokemon_name = 'bulbasaur' # change this to whatever pokemon you want

response = requests.get(
    f'https://pokemondb.net/pokedex/{pokemon_name}/moves/1')

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table")


typephysical = table.find_all(attrs={"data-sort-value": "physical"})
typespecial = table.find_all(attrs={"data-sort-value": "special"})
typestatus = table.find_all(attrs={"data-sort-value": "status"})

for element in typephysical:
    element.insert(0, NavigableString("physical"))

for element in typespecial:
    element.insert(0, NavigableString("special"))

for element in typestatus:
    element.insert(0, NavigableString("status"))


with open("randomfile.json", "a") as o:
    o.write(html_to_json(table))