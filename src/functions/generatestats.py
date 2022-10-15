import requests
from bs4 import BeautifulSoup, NavigableString
from pathlib import Path
from htmltojson import *


def generate_stats(outputFile):
    link = 'https://pokemondb.net/pokedex/all'
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find("table")

    with open(outputFile, "a") as o:
        o.write(html_to_json(table))