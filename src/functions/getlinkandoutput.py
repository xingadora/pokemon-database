import functions.generatestats
from pathlib import Path

def getlinkandoutput(generation):

    match generation:
        case 'all':
            link = 'https://pokemondb.net/pokedex/all'
            path = Path('output/all/stats.json')
        case '1':
            link = 'https://pokemondb.net/pokedex/stats/gen1'
            path = Path('output/gen1/stats.json')
        case '2':
            link = 'https://pokemondb.net/pokedex/stats/gen2'
            path = Path('output/gen2/stats.json')
        case '3':
            link = 'https://pokemondb.net/pokedex/stats/gen3'
            path = Path('output/gen3/stats.json')
        case '4':
            link = 'https://pokemondb.net/pokedex/stats/gen4'
            path = Path('output/gen4/stats.json')
        case '5':
            link = 'https://pokemondb.net/pokedex/stats/gen5'
            path = Path('output/gen5/stats.json')
        case '6':
            link = 'https://pokemondb.net/pokedex/stats/gen6'
            path = Path('output/gen6/stats.json')
        case '7':
            link = 'https://pokemondb.net/pokedex/stats/gen7'
            path = Path('output/gen7/stats.json')
        case '8':
            link = 'https://pokemondb.net/pokedex/stats/gen8'
            path = Path('output/gen8/stats.json')



    functions.generatestats.outputFile = path
    functions.generatestats.link = link