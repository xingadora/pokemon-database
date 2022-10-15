import json
from pathlib import Path
from functions.htmltojson import *
from functions.generatelearnset import *

names = Path('/data/pokemonlist.txt')


with open(names, 'r') as myfile:
    data = myfile.read()

pokemonlist = json.loads(data)


generation = '1'
outputFile = Path('output/all/learnsets.json')


generate_learnset(pokemonlist, generation, outputFile)


with open(outputFile, "a") as o:
    o.write("[")

for pokemon in pokemonlist:
    pokemon_name = pokemon['name']
    generate_learnset(pokemon_name, generation, outputFile)

with open(outputFile, "a") as o:
    o.write("{" + "}]")
