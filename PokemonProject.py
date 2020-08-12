import pprint
pokemon = {} #Empty dictionary for pokemon to be stored
#test if commit2 worked

def FindType(): #Function used to find specific types of pokemon
    findtype = input("what type are you looking for?")
    print()
    for i in pokemon:
        if pokemon[i]['Type'] == findtype: #Used to search for pokemon in pokedex on their type goes through the count of pokemon
         pprint.pprint(pokemon[i])
         print()
        if pokemon[i]['Type2'] == findtype: #Used to search for pokemon in pokedex on their type goes through the count of pokemons second typing
         pprint.pprint(pokemon[i])
         print()


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

pokemon['010'] = {'dex': '010',
                        'Name': 'Caterpie',
                        'Type': 'Bug',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['011'] = {'dex': '011',
                        'Name': 'Metapod',
                        'Type': 'Bug',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['012'] = {'dex': '012',
                        'Name': 'Butterfree',
                        'Type': 'Bug',
                        'Type2': 'Flying',
                        'Mega': 'Y'}

pokemon['013'] = {'dex': '013',
                        'Name': 'Weedle',
                        'Type': 'Bug',
                        'Type2': 'Poison',
                        'Mega': 'N'}

pokemon['014'] = {'dex': '014',
                        'Name': 'Kakuna',
                        'Type': 'Bug',
                        'Type2': 'Poison',
                        'Mega': 'N'}

pokemon['015'] = {'dex': '015',
                        'Name': 'Beedrill',
                        'Type': 'Bug',
                        'Type2': 'Poison',
                        'Mega': 'Y'}                    

pokemon['016'] = {'dex': '016',
                        'Name': 'Pigey',
                        'Type': 'Normal',
                        'Type2': 'Flying',
                        'Mega': 'N'}

pokemon['017'] = {'dex': '017',
                        'Name': 'Pigeotto',
                        'Type': 'Normal',
                        'Type2': 'Flying',
                        'Mega': 'N'}

pokemon['018'] = {'dex': '018',
                        'Name': 'Pigeot',
                        'Type': 'Normal',
                        'Type2': 'Flying',
                        'Mega': 'Y'}   

pokemon['019'] = {'dex': '019',
                        'Name': 'Rattata',
                        'Type': 'Normal',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['020'] = {'dex': '020',
                        'Name': 'Raticate',
                        'Type': 'Normal',
                        'Type2': '',
                        'Mega': 'N'} 

pokemon['021'] = {'dex': '021',
                        'Name': 'Spearow',
                        'Type': 'Normal',
                        'Type2': 'Flying',
                        'Mega': 'N'}   

pokemon['022'] = {'dex': '022',
                        'Name': 'Fearow',
                        'Type': 'Normal',
                        'Type2': 'Flying',
                        'Mega': 'N'}

pokemon['023'] = {'dex': '023',
                        'Name': 'Ekans',
                        'Type': 'Poison',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['024'] = {'dex': '024',
                        'Name': 'Arbok',
                        'Type': 'Poison',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['025'] = {'dex': '025',
                        'Name': 'Pikachu',
                        'Type': 'Electric',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['026'] = {'dex': '026',
                        'Name': 'Raichu',
                        'Type': 'Electric',
                        'Type2': '',
                        'Mega': 'N'} 

pokemon['027'] = {'dex': '027',
                        'Name': 'Sandshrew',
                        'Type': 'Ground',
                        'Type2': '',
                        'Mega': 'N'} 

pokemon['028'] = {'dex': '028',
                        'Name': 'Sandslash',
                        'Type': 'Ground',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['029'] = {'dex': '029',
                        'Name': 'Nidoran♀',
                        'Type': 'Poison',
                        'Type2': '',
                        'Mega': 'N'} 

pokemon['030'] = {'dex': '030',
                        'Name': 'Nidorina',
                        'Type': 'Poison',
                        'Type2': '',
                        'Mega': 'N'} 

pokemon['031'] = {'dex': '031',
                        'Name': 'Nidoqueen',
                        'Type': 'Poison',
                        'Type2': 'Ground',
                        'Mega': 'N'} 

pokemon['032'] = {'dex': '032',
                        'Name': 'Nidoran♂',
                        'Type': 'Poison',
                        'Type2': '',
                        'Mega': 'N'} 

pokemon['033'] = {'dex': '033',
                        'Name': 'Nidorino',
                        'Type': 'Poison',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['034'] = {'dex': '034',
                        'Name': 'Nidoking',
                        'Type': 'Poison',
                        'Type2': 'Ground',
                        'Mega': 'N'}

pokemon['035'] = {'dex': '035',
                        'Name': 'Clefairy',
                        'Type': 'Fairy',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['036'] = {'dex': '036',
                        'Name': 'Clefable',
                        'Type': 'Fairy',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['037'] = {'dex': '037',
                        'Name': 'Vulpix',
                        'Type': 'Fire',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['038'] = {'dex': '038',
                        'Name': 'Ninetales',
                        'Type': 'Fire',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['039'] = {'dex': '039',
                        'Name': 'Jigglypuff',
                        'Type': 'Normal',
                        'Type2': 'Fairy',
                        'Mega': 'N'}

pokemon['040'] = {'dex': '040',
                        'Name': 'Wigglytuff',
                        'Type': 'Normal',
                        'Type2': 'Fairy',
                        'Mega': 'N'}

pokemon['041'] = {'dex': '041',
                        'Name': 'Zubat',
                        'Type': 'Poison',
                        'Type2': 'Flying',
                        'Mega': 'N'}

pokemon['042'] = {'dex': '042',
                        'Name': 'Golbat',
                        'Type': 'Poison',
                        'Type2': 'Flying',
                        'Mega': 'N'}

pokemon['043'] = {'dex': '043',
                        'Name': 'Oddish',
                        'Type': 'Poison',
                        'Type2': 'Poison',
                        'Mega': 'N'}

pokemon['044'] = {'dex': '044',
                        'Name': 'Gloom',
                        'Type': 'Grass',
                        'Type2': 'Poison',
                        'Mega': 'N'}

pokemon['045'] = {'dex': '045',
                        'Name': 'Vileplume',
                        'Type': 'Grass',
                        'Type2': 'Poison',
                        'Mega': 'N'}

pokemon['046'] = {'dex': '046',
                        'Name': 'Paras',
                        'Type': 'Bug',
                        'Type2': 'Grass',
                        'Mega': 'N'}

pokemon['047'] = {'dex': '047',
                        'Name': 'Parasect',
                        'Type': 'Bug',
                        'Type2': 'Grass',
                        'Mega': 'N'}

pokemon['048'] = {'dex': '048',
                        'Name': 'Venonat',
                        'Type': 'Bug',
                        'Type2': 'Poison',
                        'Mega': 'N'}

pokemon['049'] = {'dex': '049',
                        'Name': 'Venomoth',
                        'Type': 'Bug',
                        'Type2': 'Poison',
                        'Mega': 'N'}

pokemon['050'] = {'dex': '050',
                        'Name': 'Diglett',
                        'Type': 'Ground',
                        'Type2': '',
                        'Mega': 'N'}

pokemon['051'] = {'dex': '051',
                        'Name': 'Dugtrio',
                        'Type': 'Ground',
                        'Type2': '',
                        'Mega': 'N'}

FindType()