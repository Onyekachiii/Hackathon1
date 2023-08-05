import time
import numpy as np
import sys
import json

# Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print("~~~~~Welcome to Pokémon Arcade Lite~~~~~\n")
Player1 = input("Player1 enter your name: ") or "This hooman hopefully its a human O>O, is way wayyy wayyyyyyyyyyyyyy too lazy to put a name and think they are funny so this will be your name now and no most certainly not you cannot change your name ;>"
Player2 = input("Player2 enter your name: ") or "This hooman hopefully its a human O>O, is way wayyy wayyyyyyyyyyyyyy too lazy to put a name and think they are funny so this will be your name now and no most certainly not you cannot change your name ;>"

class Pokemon:
    def __init__(self, name, types, moves, EVs, health='===================='):
        self.name = name
        self.types = types  # Make sure this is a single string, not a list
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20  # Amount of health bars

    def fight(self, Pokemon2):
        delay_print(f"{Player1} challenges {Player2}\n")
        delay_print("\n~~~~POKEMON BATTLE~~~~~")
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

        type_advantages = {
            'Normal': ['Rock', 'Steel'],
            'Fire': ['Grass', 'Ice', 'Bug', 'Steel'],
            'Water': ['Fire', 'Ground', 'Rock'],
            'Electric': ['Water', 'Flying'],
            'Grass': ['Water', 'Ground', 'Rock'],
            'Ice': ['Grass', 'Ground', 'Flying', 'Dragon'],
            'Fighting': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'],
            'Poison': ['Grass', 'Fairy'],
            'Ground': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'],
            'Flying': ['Grass', 'Fighting', 'Bug'],
            'Psychic': ['Fighting', 'Poison'],
            'Bug': ['Grass', 'Psychic', 'Dark'],
            'Rock': ['Fire', 'Ice', 'Flying', 'Bug'],
            'Ghost': ['Psychic', 'Ghost'],
            'Dragon': ['Dragon'],
            'Dark': ['Psychic', 'Ghost'],
            'Steel': ['Ice', 'Rock', 'Fairy'],
            'Fairy': ['Fighting', 'Dragon', 'Dark']
        }
        delay_print(f"\n{Player1}: Go {self.name}, I choose you!\n")
        delay_print(f"\n{Player2}: Go {Pokemon2.name}, I choose you!\n")
        while self.bars > 0 and Pokemon2.bars > 0:
            money = np.random.choice(1000)
            delay_print(f"\n{self.name}: \n")
            delay_print(f"HLTH:     {self.health}\n")
            delay_print(f"\n{Pokemon2.name}: \n")
            delay_print(f"HLTH:     {Pokemon2.health}\n")
            #
            #
            #
            player1_type = self.types
            player2_type = Pokemon2.types
            delay_print(f"\n{Player1}: {self.name}, Use: ")
            try:
                for i, move in enumerate(self.moves):
                    delay_print(f"\n{i + 1}. {move}  ")
                move_choice = int(input("\nEnter the number of the move you want to use: ")) - 1
                selected_move = self.moves[move_choice]
                delay_print(f"{self.name} used {selected_move}")
            except (IndexError, ValueError):
                delay_print("Invalid input. Please pick a valid move.Since you are someone who doesnt understand basic english we skipped your turn and  selected a random move. :)")
            # Determine effectiveness for Player 2
            try:
                if player1_type in type_advantages:
                    if player2_type in type_advantages[player1_type]:
                        delay_print("\nSuper effective!")
                        Pokemon2.health = Pokemon2.health[:-10]  # Reduce health by 10 characters
                    else:
                        delay_print("\nNot very effective.")
                        Pokemon2.health = Pokemon2.health[:-5]
            except (IndexError, ValueError):
                delay_print("Invalid input. Please pick a valid move.Since you are someone who doesnt understand basic english we skipped your turn and  selected a random move. :)")
            
            if len(Pokemon2.health) == 0:
                delay_print(f"\n{Pokemon2.name} fainted. {Player1} wins!\n")
                delay_print(f"\n{Player2} paid {Player1} ${money}.\n")
                break
            #
            #
            #
            time.sleep(1)
            delay_print(f"\n{self.name}: \n")
            delay_print(f"HLTH:     {self.health}\n")
            delay_print(f"\n{Pokemon2.name}: \n")
            delay_print(f"HLTH:     {Pokemon2.health}\n")
            time.sleep(0.5)

            if Pokemon2.bars <= 0:
                delay_print(f"\n{Pokemon2.name} fainted. {Player1} wins!\n")
                delay_print(f"\n{Player2} paid {Player1} ${money}.\n")
                return
            #
            #
            #
            delay_print(f"\n{Player2}: {Pokemon2.name}, Use: ")
            try:
                for i, move in enumerate(Pokemon2.moves):
                    delay_print(f"\n{i + 1}. {move}  ")
                move_choice = int(input("\nEnter the number of the move you want to use: ")) - 1
                selected_move = Pokemon2.moves[move_choice]
                delay_print(f"{Pokemon2.name} used {selected_move}")
            except (IndexError, ValueError):
                delay_print("Invalid input. Please pick a valid move.Since you are someone who doesnt understand basic english we skipped your turn and  selected a random move. :)")
            # Determine effectiveness for Player 2
            try:
                if player2_type in type_advantages:
                    if player1_type in type_advantages[player2_type]:
                        delay_print("\nSuper effective!")
                        self.health = self.health[:-10]  # Reduce health by 10 characters
                    else:
                        delay_print("\nNot very effective.")
                        self.health = self.health[:-5]
            except (IndexError, ValueError):
                delay_print("Invalid input. Please pick a valid move.Since you are someone who doesnt understand basic english we skipped your turn and  selected a random move. :)")
            
            if len(self.health) == 0:
                delay_print(f"\n{self.name} fainted. {Player2} wins!\n")
                delay_print(f"\n{Player1} paid {Player2} ${money}.\n")
                break
            

if __name__ == '__main__':
    with open('pokemon_data.json', 'r') as f:
        pokemon_data = json.load(f)

    Charizard = Pokemon(**pokemon_data["Charizard"])
    Blastoise = Pokemon(**pokemon_data["Blastoise"])
    Venusaur = Pokemon(**pokemon_data["Venusaur"])
    Charmander = Pokemon(**pokemon_data["Charmander"])
    Squirtle = Pokemon(**pokemon_data["Squirtle"])
    Bulbasaur = Pokemon(**pokemon_data["Bulbasaur"])
    Charmeleon = Pokemon(**pokemon_data["Charmeleon"])
    Wartortle = Pokemon(**pokemon_data["Wartortle"])
    Ivysaur = Pokemon(**pokemon_data["Ivysaur"])
    Pikachu = Pokemon(**pokemon_data["Pikachu"])
    Jigglypuff = Pokemon(**pokemon_data["Jigglypuff"])
    Geodude = Pokemon(**pokemon_data["Geodude"])
    Machop = Pokemon(**pokemon_data["Machop"])
    Gastly = Pokemon(**pokemon_data["Gastly"])
    Abra = Pokemon(**pokemon_data["Abra"])
    Growlithe = Pokemon(**pokemon_data["Growlithe"])
    Slowpoke = Pokemon(**pokemon_data["Slowpoke"])
    Magnemite = Pokemon(**pokemon_data["Magnemite"])
    Doduo = Pokemon(**pokemon_data["Doduo"])
    Seel = Pokemon(**pokemon_data["Seel"])
    Grimer = Pokemon(**pokemon_data["Grimer"])
    Onix = Pokemon(**pokemon_data["Onix"])
    Caterpie = Pokemon(**pokemon_data["Caterpie"])
    Weedle = Pokemon(**pokemon_data["Weedle"])
    Pidgey = Pokemon(**pokemon_data["Pidgey"])
    Rattata = Pokemon(**pokemon_data["Rattata"])
    Spearow = Pokemon(**pokemon_data["Spearow"])
    Ekans = Pokemon(**pokemon_data["Ekans"])
    Sandshrew = Pokemon(**pokemon_data["Sandshrew"])
    NidoranF = Pokemon(**pokemon_data["Nidoranf"])
    NidoranM = Pokemon(**pokemon_data["Nidoranm"])
    Clefairy = Pokemon(**pokemon_data["Clefairy"])
    Vulpix = Pokemon(**pokemon_data["Vulpix"])
    Zubat = Pokemon(**pokemon_data["Zubat"])
    Oddish = Pokemon(**pokemon_data["Oddish"])
    Paras = Pokemon(**pokemon_data["Paras"])
    Venonat = Pokemon(**pokemon_data["Venonat"])
    Diglett = Pokemon(**pokemon_data["Diglett"])
    Meowth = Pokemon(**pokemon_data["Meowth"])
    Psyduck = Pokemon(**pokemon_data["Psyduck"])
    Mankey = Pokemon(**pokemon_data["Mankey"])
    Poliwag = Pokemon(**pokemon_data["Poliwag"])
    Bellsprout = Pokemon(**pokemon_data["Bellsprout"])
    Tentacool = Pokemon(**pokemon_data["Tentacool"])
    Tentacool.fight(Charizard)
