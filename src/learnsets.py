import json
from functions.htmltojson import *
from functions.generatelearnset import *


with open('src\data\pokemonnames.json', 'r') as myfile:
    data = myfile.read()

pokemonlist = json.loads(data)


generation = '1'
outputFile = f'output\gen{generation}\learnsets.json'


generate_learnset(pokemonlist, generation, outputFile)


with open(outputFile, "a") as o:
    o.write("[")

for pokemon in pokemonlist:
    pokemon_name = pokemon['name']
    generate_learnset(pokemon_name, generation, outputFile)

with open(outputFile, "a") as o:
    o.write("{" + "}]")
