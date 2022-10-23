from dataclasses import dataclass
from functions.htmltojson import *
import requests
from bs4 import BeautifulSoup, NavigableString
import json
from pathlib import Path

outputFile = Path('output/gen1/learnset.json')
names = Path('src/data/pokemonlist.json')

f = open(names)
data = json.load(f)
names = data[0:151]


def getLearnset(pokemon_name):

    response = requests.get(
        f'https://pokemondb.net/pokedex/{pokemon_name}/moves/1')

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.table
    rows = table.find_all('tr')


    def td():
        for row in rows[1:]:
            yield "<th>" + row.td.text + "</th>"


    def tr():
        for row in rows[1:]:
            yield "<td>" + row.a.text + "</td>"


    top = "<table>" + "<thead>" + "<tr>"
    tds = list(td())
    mid = "</tr>" + "</thead>" + "<tbody>" + "<tr>"
    trs = list(tr())
    bot = "</tr>" + "</tbody>" + "</table>"

    html = top + "".join(tds) + mid + "".join(trs) + bot
    htmlF = BeautifulSoup(html, 'html.parser')


    with open(outputFile, "a") as o:
        o.write('{"' + pokemon_name + '":')
        o.write(html_to_json(htmlF))
        o.write('},')


# use wrap() !!!!!!!!!!!!!!!
with open(outputFile, "a") as o:
    o.write('[')

for name in names:
    getLearnset(name)

with open(outputFile, "a") as o:
    o.write(']')