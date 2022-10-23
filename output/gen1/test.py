import json
from pathlib import Path


outputFile = Path('output/gen1/learnset.json')


f = open(outputFile)
data = json.load(f)


bulbasaur = data['bulbasaur'][0]


lvl = 99

print(str(lvl))

for i in bulbasaur:
    if i < str(lvl):
        print(i + ": " + bulbasaur[i])