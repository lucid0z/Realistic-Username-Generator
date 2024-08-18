import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

first_words = ["Crazy", "Sky", "Dragon", "Mystick", "Just", "Shadow", "Cyber", "legendary", "Starry", "dark", "Sly", "Aero", "Neo", "Mine"]
second_words = ["gamer", "walker", "Slayer", "Wizard", "Master", "Hunter", "Knight", "Hero", "Commander", "Phoenix", "Shadow"]

advanced_prename = [
    "FaZe_", "Neo", "Gmd", "Not", "fw", "Xx", "z", "f", "vv", 'x',
    "Real", "Its", "Itz", "qq", "Sir"
    ]
advanced_username = [
    "Klix", "Flux", "Crimson", "Fusion", "Nebula", "Zephyr", "Flux", "Nova",
    "Switch", "Cypher", "Fanum", "Apollo", "K1ng", "Robin", "Skull", "Dummy",
    "Polo", "Rover", "tunde", "AN0NYMOUS", "Crvzy", "Crxzy", "Aura", "Sharky",
    "Vertex", "Rogue", "Zenith", "Blaze", "Echo", "Maverick", "Specter", "Zeal",
    "Phantom", "Vortex", "Onyx", "Nexxus", "Drake", "Havoc", "Striker", "Viper",
    "Rynex", "Rex", "Shadow", "Inferno", "Tempest", "Xero", "Kryptic", "Volt",
    "Fury", "Jinx", "Sable", "Quasar", "NovaX", "Vanguard", "Alpha", "Titan",
    "Nyx", "Bolt", "Enigma", "Zen", "Karma", "Gravix", "Surge", "Artemis",
    "Void", "Flask",
]
advanced_endname = [
    "WasTaken", "XX", "X", "GmD", "Z", "01", "IsHere",
    "FR", 'TK', "V2", "V3", "FN", "3rd", "WRLD"
    ]

def gen_basic_username():
    # basic usernames
    chosen_username = random.choice(first_words) + random.choice(second_words)
    numbIndex = random.randint(1,2)
    
    if numbIndex == 1:
       chosen_username = chosen_username + str(random.randint(1,524))          

    return chosen_username

def gen_real_username():
    # more advanced usernames, could be "taken" on websites
    numbIndex = random.randint(1,2)

    if numbIndex == 1:
       # use prename
       chosen_username = random.choice(advanced_prename) + random.choice(advanced_username)
       return chosen_username

    if numbIndex == 2:
        # use endname
        chosen_username = random.choice(advanced_username) + random.choice(advanced_endname)
        return chosen_username

print(gen_real_username())
