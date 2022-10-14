from htmltojson import *
from learnsets import *
import requests
from bs4 import BeautifulSoup, NavigableString
import json


# with open('src\pokemonstats.json', 'r') as myfile:
# data = myfile.read()

# pokemonlist = json.loads(data)


# def unf_generate_learnset(pokemon_name):

pokemon_name = 'bulbasaur'

response = requests.get(
    f'https://pokemondb.net/pokedex/{pokemon_name}/moves/1')  # the 1 at the end is for gen 1

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.table
rows = table.find_all('tr')

# print("<table>" + "<thead>" + "<tr>")
# for row in rows[1:]:
#     print("<th>" + row.td.text + "</th>")
# print("</tr>" + "</thead>" + "<tbody>" + "<tr>")
# for row in rows[1:]:
#     print("<td>" + row.a.text + "</td>")
# print("</tr>" + "</tbody>" + "</table>")


# for pokemon in pokemonlist:
# pokemon_name = pokemon['name']
# print(pokemon_name)
# unf_generate_learnset(pokemon_name)

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


html = top + ''.join(tds) + mid + ''.join(trs) + bot

print(html)