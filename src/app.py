import requests
from bs4 import BeautifulSoup


pokemon_name = 'pikachu'
response = requests.get(f'https://pokemondb.net/pokedex/{pokemon_name}/moves/1')

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)