
# PokémonDB JSON Files

This is a collection of JSON files which contain stats and information for all current Pokémon generations and games.


## Credit
All of the data in this repo is from [PokémonDB](https://pokemondb.net/)

Usage of this data falls under Pokémon copyright:

_© 2022 Pokémon. © 1995–2022 Nintendo/Creatures Inc./GAME FREAK inc. Pokémon, Pokémon character names, Nintendo Switch, Nintendo 3DS, Nintendo DS, Wii, Wii U, and WiiWare are trademarks of Nintendo. The YouTube logo is a trademark of Google Inc. Other trademarks are the property of their respective owners.

_Distribution in any form and any channels now known or in the future of derivative works based on the copyrighted property trademarks, service marks, trade names and other proprietary property (Fan Art) of The Pokémon Company International, Inc., its affiliates and licensors (Pokémon) constitutes a royalty-free, non-exclusive, irrevocable, transferable, sub-licensable, worldwide license from the Fan Art's creator to Pokémon to use, transmit, copy, modify, and display Fan Art (and its derivatives) for any purpose. No further consideration or compensation of any kind will be given for any Fan Art. Fan Art creator gives up any claims that the use of the Fan Art violates any of their rights, including moral rights, privacy rights, proprietary rights publicity rights, rights to credit for material or ideas or any other right, including the right to approve the way such material is used. In no uncertain terms, does Pokémon's use of Fan Art constitute a grant to Fan Art's creator to use the Pokémon intellectual property or Fan Art beyond a personal, noncommercial home use.


## Data
All the data can be found in the [output folder](https://github.com/xingadora/pokemon-database/tree/main/output).
## Running Locally
#### If you would like to use this program to generate specified data not already in the output folder, follow the steps below:

Clone the project

```bash
  git clone https://github.com/xingadora/pokemon-database
```

Go to the project directory

```bash
  cd pokemon-database
```

Install dependencies

```bash
  pip install -r requirements.txt
```

#### Once you have cloned the repo and installed the dependencies, you can either run the main file (the output from which is already stored in the output folder), or configure the python files to get your desired results.

To run the main file

```bash
  pip -u generator.py
```
## Customizing

Within the `src` folder, generatoralt.py, and learnsets.py contain partially completed code that can be customized. Inside the `src/functions` folder, generatelearnset.py can also be customized.

generatestats.py is already run from the generator.py file.