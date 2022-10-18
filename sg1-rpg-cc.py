import sys, random

races = ['ATUREN', 'HUMAN', 'JAFFA', 'TOKRA', 'UNAS']
classes = ['DIPLOMAT', 'ENGINEER', 'MEDIC', 'SCIENTIST', 'SCOUT', 'SOLDIER']
origins = ['BIOME', 'BACKGROUND', 'RACIAL']
biomes = ['ARBOREAL', 'ARTIFICIAL', 'DESERT', 'GRASSLANDS', 'LUNAR',
'MOUNTAINOUS', 'OCEANIC', 'RAINFOREST', 'STARSHIP', 'TERRAFORMED',
'TOXIC', 'TUNDRA', 'SUBTERRANEAN', 'SWAMP', 'URBAN', 'VOLCANIC']
backgrounds = ['AVIATOR', 'DRIVER', 'ENTERTAINER', 'ENFORCEMENT', 'ENSLAVED',
'FORMER HOST', 'FREEDOM FIGHTER', 'HEALER', 'HERDSMAN', 'HUNTER/GATHERER',
'LIAISON', 'MERCHANT', 'MILITARY', 'PRESERVATIONIST', 'POLITICIAN',
'REFUGEE', 'SAILOR', 'SCHOLAR', 'SENTRY', 'SLEUTH',
'STUDENT', 'SWINDLER', 'TEACHER', 'WRIGHT', 'UNDERWORLD']
racials = ['ATUREN SPIRITUALIST', 'JAFFA RENEGADE', 'STUDENT OF BRATAC',
'TAURI MILITARY', 'TOKRA SPY', 'UNAS ALPHA']

race = races[random.randrange(len(races))]
class1 = classes[random.randrange(len(classes))]
ochoices = random.sample(range(0,3), 2)
origin1 = origins[ochoices[0]]
origin2 = origins[ochoices[1]]

if origin1 == 'BIOME':
    specorigin1 = biomes[random.randrange(len(biomes))]
elif origin1 == 'BACKGROUND':
    specorigin1 = backgrounds[random.randrange(len(backgrounds))]
elif origin1 == 'RACIAL':
    if race == 'ATUREN':
        specorigin1 = 'ATUREN SPIRITUALIST'
    elif race == 'JAFFA':
        specorigin1 = racials[random.randrange(1,3)]
    elif race == 'HUMAN':
        specorigin1 = 'TAURI MILITARY'
    elif race == 'TOKRA':
        specorigin1 = 'TOKRA SPY'
    elif race == 'UNAS':
        specorigin1 = 'UNAS ALPHA'

if origin2 == 'BIOME':
    specorigin2 = biomes[random.randrange(len(biomes))]
elif origin2 == 'BACKGROUND':
    specorigin2 = backgrounds[random.randrange(len(backgrounds))]
elif origin2 == 'RACIAL':
    if race == 'ATUREN':
        specorigin2 = 'ATUREN SPIRITUALIST'
    elif race == 'JAFFA':
        specorigin2 = racials[random.randrange(1,2)]
    elif race == 'HUMAN':
        specorigin2 = 'TAURI MILITARY'
    elif race == 'TOKRA':
        specorigin2 = 'TOKRA SPY'
    elif race == 'UNAS':
        specorigin2 = 'UNAS ALPHA'

print(f'''
COMTRYA!

Welcome to the Stargate SG-1 Roleplaying Game Random Character Creator

Your race is {race}

Your class is {class1}

Your origins are {origin1}: {specorigin1} and {origin2}: {specorigin2}
''')

a = input('Press ENTER to exit\n')
if a:
    sys.exit()
