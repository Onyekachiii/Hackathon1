import time
import numpy as np
import sys

# Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

Player1 = input("Player1 enter your name: ") or "This human hopefully its a human O>O, is way wayyy wayyyyyyyyyyyyyy too lazy to put a name and think they are funny so this will be your name now and no most certainly not you cannot change your name ;>"
Player2 = input("Player2 enter your name: ") or "This human hopefully its a human O>O, is way wayyy wayyyyyyyyyyyyyy too lazy to put a name and think they are funny so this will be your name now and no most certainly not you cannot change your name ;>"

# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='================================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20  # Amount of health bars

    def fight(self, Pokemon2):
        delay_print(f"{Player1} challenges {Player2}\n")
        delay_print("\n-----POKEMON BATTLE-----")
        delay_print(f"\n{Player1} chooses {self.name}")
        delay_print(f"\nTYPE/{self.types}")
        delay_print(f"\nATTACK/{self.attack}")
        delay_print(f"\nDEFENSE/{self.defense}")
        delay_print(f"\nLVL/{3 * (1 + np.mean([self.attack, self.defense]))}\n")
        delay_print("\nVS\n")
        delay_print(f"\n{Player2} chooses {Pokemon2.name}")
        delay_print(f"\nTYPE/{Pokemon2.types}")
        delay_print(f"\nATTACK/{Pokemon2.attack}")
        delay_print(f"\nDEFENSE/{Pokemon2.defense}")
        delay_print(f"\nLVL/{3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense]))}\n")

        time.sleep(2)

        version = ['Fire', 'Water', 'Grass']
        for i, k in enumerate(version):
            if self.types == k:
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'
                if Pokemon2.types == version[(i + 1) % 3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'
                if Pokemon2.types == version[(i + 2) % 3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'
        delay_print(f"\n{Player1}:Go {self.name}!\n")
        delay_print(f"\n{Player2}:Go {Pokemon2.name}!\n")
        while self.bars > 0 and Pokemon2.bars > 0:
            money = np.random.choice(1000)
            delay_print(f"\n{self.name}: \n")
            delay_print(f"HLTH:     {self.health}\n")
            delay_print(f"\n{Pokemon2.name}: \n")
            delay_print(f"HLTH:     {Pokemon2.health}\n")

            delay_print(f"\n{Player1}:{self.name}, Use: ")
            for i, x in enumerate(self.moves):
                delay_print(f"\n{i + 1}. {x}")
            try:
                index = int(input('\nPick a move: '))
                delay_print(f"\n{self.name} used {self.moves[index - 1]}!")
                time.sleep(1)
                delay_print(f"\n{string_1_attack}")
            except (IndexError, ValueError):
                delay_print("Invalid input. Please pick a valid move.Since you are someone who doesnt understand basic english we skipped your turn and  selected a random move. :)")

            Pokemon2.bars -= self.attack
            Pokemon2.health = "=" * int(Pokemon2.bars + 0.1 * Pokemon2.defense)

            for j in range(int(Pokemon2.bars + 0.1 * Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            delay_print(f"\n{self.name}: \n")
            delay_print(f"HLTH:     {self.health}\n")
            delay_print(f"\n{Pokemon2.name}: \n")
            delay_print(f"HLTH:     {Pokemon2.health}\n")
            time.sleep(0.5)

            if Pokemon2.bars <= 0:
                delay_print(f"\n{Pokemon2.name} fainted. {Player1} win!\n")
                delay_print(f"\n{Player2} paid {Player1} ${money}.\n")
                return
            delay_print(f"\n{Player2}: {Pokemon2.name}, Use: ")
            for i, x in enumerate(Pokemon2.moves):
                delay_print(f"\n{i + 1}. {x}")
            try:
                index = int(input('\nPick a move: '))
                delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index - 1]}!")
                time.sleep(1)
                delay_print(f"\n{string_2_attack}")
            except (IndexError, ValueError):
                delay_print("Invalid input. Please pick a valid move.Since you are someone who doesnt understand basic english we skipped your turn and  selected a random move. :)")

            self.bars -= Pokemon2.attack
            self.health = "=" * int(self.bars + 0.1 * self.defense)

            for j in range(int(self.bars + 0.1 * self.defense)):
                self.health += "="

            if self.bars <= 0:
                delay_print(f"\n{self.name} fainted. {Player2} wins!\n")
                delay_print(f"\n{Player1} paid {Player2} ${money}.\n")
                return

if __name__ == '__main__':
    # Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK': 12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK': 10, 'DEFENSE': 10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {'ATTACK': 8, 'DEFENSE': 12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], {'ATTACK': 4, 'DEFENSE': 2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'ATTACK': 3, 'DEFENSE': 3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'], {'ATTACK': 2, 'DEFENSE': 4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'], {'ATTACK': 6, 'DEFENSE': 5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'], {'ATTACK': 5, 'DEFENSE': 5})
    Ivysaur = Pokemon('Ivysaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'], {'ATTACK': 4, 'DEFENSE': 6})

    Ivysaur.fight(Squirtle) # Get them to fight
