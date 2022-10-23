import requests
from bs4 import BeautifulSoup, NavigableString
# from .htmltojson import html_to_json
from pathlib import Path

outputFile = Path('output/gen1/learnset.json')


def generate_learnset(pokemon_name, generation, learntype, outputFile):
    link = f'https://pokemondb.net/pokedex/{pokemon_name}/moves/{generation}'

    response = requests.get(link)

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

    print(table.encode("utf-8"))
    

    """ with open(outputFile, "a") as o:
        o.write('{"' + pokemon_name + '":')
        o.write(html_to_json(table))
        o.write('},') """


generate_learnset('bulbasaur', '1', 'level-up', outputFile)