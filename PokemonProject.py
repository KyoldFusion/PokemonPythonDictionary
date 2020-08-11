import pprint
pokemon = {} #Empty dictionary for pokemon to be stored
#test if commit worked

def FindType(): #Function used to find specific types of pokemon
    findtype = input("what type are you looking for?")
    for i in pokemon:
        if pokemon[i]['Type'] == findtype: #Used to search for pokemon in pokedex on their type goes through the count of pokemon
         pprint.pprint(pokemon[i])
        if pokemon[i]['Type2'] == findtype: #Used to search for pokemon in pokedex on their type goes through the count of pokemons second typing
         pprint.pprint(pokemon[i])


Types = ['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dark', 'Dragon', 'Steel', 'Fairy'] # Set of the different pokemon types
pokemon['001'] = {'dex': '001', # Pokedex Number
                        'Name': 'Bulbasaur', #Pokemon Name
                        'Type': 'Grass', #Pokemon Type1
                        'Type2': 'Poison', #Pokemon Type2 (Uses '' if it is a monotype for FindType Function to work properly through dictionary)
                        'Mega': 'N'} #Is the pokemon able to mega evolve (N) if no (Y) if yes

pokemon['002'] = {'dex': '002',
                        'Name': 'Ivysaur',
                        'Type': 'Grass',
                        'Type2': 'Poison',
                        'Mega': 'N'}

pokemon['003'] = {'dex': '003',
                        'Name': 'Venusaur',
                        'Type': 'Grass',
                        'Type2': 'Poison',
                        'Mega': 'Y'}

pokemon['004'] = {'dex': '004',
                        'Name': 'Charmander',
                        'Type': 'Fire',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['005'] = {'dex': '005',
                        'Name': 'Charmeleon',
                        'Type': 'Fire',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['006'] = {'dex': '006',
                        'Name': 'Charizard',
                        'Type': 'Fire',
                        'Type2': 'Flying',
                        'Mega': 'Y'}
                    
pokemon['007'] = {'dex': '007',
                        'Name': 'Squirtle',
                        'Type': 'Water',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['008'] = {'dex': '008',
                        'Name': 'Wartortle',
                        'Type': 'Water',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['009'] = {'dex': '009',
                        'Name': 'Blastoise',
                        'Type': 'Water',
                        'Type2': '',
                        'Mega': 'Y'}

FindType()