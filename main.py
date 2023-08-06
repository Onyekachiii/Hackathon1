import time #for the time pause
import numpy as np
import sys
import json # load json file
import random #for random randint

# Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, types, moves, EVs, health='===================='):
        self.name = name
        self.types = types  # Make sure this is a single string, not a list
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20  # Amount of health bars
    
    def print_colorful_ascii_art(self, art, color='white'):
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',         # for color
            'purple': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m'
        }
        end_color = '\033[0m'
        print(colors[color] + art + end_color)


    def introduce_game_with_storyline(self,Pokemon2,Player1,Player2):
        self.print_colorful_ascii_art("\nWelcome to Pokémon Arcade DEMO!", 'green')
        delay_print("\nYou are embarking on a journey to save the legendary Pokémon Arconia.")
        delay_print("Legend has it that Arconia possesses immense power to \nprotect the Pokémon world.")
        delay_print("But it is under threat from the evil Team Darkstorm.")
        delay_print("You must gather the strongest Pokémon and \ndefeat Team Darkstorm to save Arconia.")
        delay_print("\nYour adventure begins...\n")
        delay_print("\nProfessor Juniper:Ah you've made it..")
        #boy or girl
        boy_or_girl = input("\nAre you a 'Boy' or a 'Girl'?: ")
        while True:
            delay_print(f"\nDo you confirm you are a {boy_or_girl}?")
            confirm = input("\nyes or no?: ")
            if confirm == "yes":
                break
            else:
                boy_or_girl = input("Are you a 'Boy' or a 'Girl'?: ")
        delay_print("\nProfessor Juniper:Umm..what is your name again?")
        #name
        Player1 = input("\nEnter your name: ") or "Alex"
        while True:
            delay_print(f"\nDo you confirm its: {Player1}?")
            confirm = input("\nyes or no?: ")
            if confirm == "yes":
                delay_print(f"\nProfessor Juniper:Alright then {Player1},I will teleport you to your house now\n")
                break
            else:
                Player1 = input("\nEnter your name: ") or "Alex"
        delay_print("\n*You wake up in your room*\n")
        delay_print(f"\nMom:{Player1}!Come downstairs quickly!")
        go_downstairs = input("\nEnter 'g' to go downstairs: \n")
        while True:
            if go_downstairs == 'g':
                delay_print(f"\n*You rushed downstairs*\n")
                break
            else:
                delay_print("\nInvalid try again.")
                go_downstairs = input("\nEnter 'g' to go downstairs: \n")
        delay_print(f"\nMom:So close hun..Your Father was in an interview on T.V")
        delay_print("\nMom:Anyways you should go meet Porfessor Juniper...Her lab is next doors")
        while True:
            go_outside = input("\nEnter 'g' to go outside: \n")
            if go_outside == 'g':
                delay_print(f"\n*You go outside and stands infront of Professor Juniper's lab door*\n")
                break
            else:
                delay_print("\nInvalid try again.")
        delay_print("\nUnkown:OUT OF THE WAY,MY MOTHER NEEDS ME!")
        delay_print(f"\n{Player1}:Geez...")
        go_inside = input("\nEnter 'e' to enter: \n")
        while True:
            if go_inside == 'e':
                delay_print(f"\n*You enter the lab and see a young girl beside Professor Juniper*\n")
                break
            else:
                delay_print("\nInvalid try again.")
                go_inside = input("\nEnter 'e' to enter: \n")
        delay_print(f"\nProfessor Juniper:Welcome {Player1},We were just waiting for you.")
        delay_print(f"\nProfessor Juniper:Meet my daughter... ... ...")
        #rival name
        Player2 = input("\nEnter your Rival's name(default:'May'): ") or "May"
        while True:
            delay_print(f"\nDo you confirm its: {Player2}?")
            confirm = input("\nyes or no?: ")
            if confirm == "yes":
                delay_print(f"\nProfessor Juniper:Meet my daughter {Player2}\n")
                break
            else:
                Player2 = input("\nEnter your Rival's name(default:'May'): ") or "May"
        if Player2 == 'May':
            delay_print(f'{Player1}:Nice to meet you... March..')
            delay_print(f"\n{Player2}:tsk...")
        else:
            delay_print(f"{Player2}:Yeah")
        delay_print(f"\nProfessor Juniper:Don't worry {Player1}, she is an angel even if she doesn't show it")
        delay_print(f"\nProfessor Juniper:Today,you two are going to start your journey today so go over the table and grab a pokemon")
        delay_print(f"\n*You move to the table and choose a pokemon*\n")
        #choose pokemon
        self.name = input(f'\nYou choose a pokemon, options are (Charmander[fire-type]),(Bulbasaur[Grass-type]),(Squirtle[Water-Type]): ')
        while True:
            delay_print(f"\nAre you sure you want to choose {self.name}?: ")
            confirm_pokemon = input(f"\nYes or No?: ")
            if confirm_pokemon == 'yes':
                break
            else:
                self.name = input(f'\n{Player1} choose a pokemon, options are (Carmender[fire-type]),(Bulbasaur[Grass-type]),(Squirtle[Water-Type]): ')
        delay_print(f'\n~~~{Player1} obtained a {self.name}~~~')
        
        
        
        #nickname
        delay_print(f"\nDo you wish to give {self.name} a nickname?")
        give_nickname = input(f"\nYes or No?: ")

        if give_nickname.lower() == 'yes':
            while True:
                self.new_name = input(f"\nWhat nickname do you want to give your {self.name}?: ")
                delay_print(f"\nAre you sure you want {self.name} to be nicknamed as {self.new_name}?")
                confirm_nickname = input("\nYes or No?: ")
                if confirm_nickname.lower() == 'yes':
                    delay_print(f"\n{self.name} is now named {self.new_name}")
                    break
        else:
            self.new_name = self.name



#rival pokemon
        if self.name == 'Charmander':
            Pokemon2.name = 'Squirtle'
            delay_print(f"\n{Player2}:Alright then I will pick Squirtle[Water-Type]")
        elif self.name == 'Squirtle':
            Pokemon2.name = 'Bulbasaur'
            delay_print(f"\n{Player2}:Alright then I will pick Bulbasaur[Grass-type]")
        else:
            Pokemon2.name = 'Charmander'
            delay_print(f"\n{Player2}:Alright then I will pick Carmender[fire-type]")
        
        delay_print(f"\nProfessor Jutiper:If you two are done choosing, come pick your pokedex and you can start adventuring into the vast world of Hoe-nn")
        delay_print(f"\n*You go to Professor Juniper and leaves the lab*\n")
        delay_print(f"\n*As you are leaving, you hear {Player2} shout your name*\n")
        
    def frist_fight(self, Pokemon2, Player1, Player2):
        delay_print(f"{Player1}, I challenge you to a pokemon battle\n")
        delay_print("\n~~~~POKEMON BATTLE~~~~~\n")
        delay_print(f"\n{self.name}")
        delay_print(f"\nTYPE/{self.types}")
        delay_print(f"\nATTACK/{self.attack}")
        delay_print(f"\nDEFENSE/{self.defense}\n")
        delay_print("\nVS\n")
        delay_print(f"\n{Pokemon2.name}")
        delay_print(f"\nTYPE/{Pokemon2.types}")
        delay_print(f"\nATTACK/{Pokemon2.attack}")
        delay_print(f"\nDEFENSE/{Pokemon2.defense}\n")

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
            money = np.random.choice(100)
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
            #
            #
            #
            delay_print(f"\n{Player2}: {Pokemon2.name}, Use: ")
            for i, move in enumerate(Pokemon2.moves):
                delay_print(f"\n{i + 1}. {move}  ")
            # Generate a random move choice
            move_choice = random.randint(1, len(Pokemon2.moves)) - 1
            selected_move = Pokemon2.moves[move_choice]
            # Display the selected move
            delay_print(f"\n{Player2}: {Pokemon2.name} used {selected_move}")
            # Determine effectiveness for Player 2
            if player2_type in type_advantages:
                if player1_type in type_advantages[player2_type]:
                    delay_print("\nSuper effective!")
                    self.health = self.health[:-10]  # Reduce health by 10 characters
                else:
                    delay_print("\nNot very effective.")
                    self.health = self.health[:-5]  # Reduce health by 5 characters
            
            if len(self.health) == 0:
                delay_print(f"\n{self.name} fainted. {Player2} wins!\n")
                delay_print(f"\n{Player1} paid {Player2} ${money}.\n")
                break
    
    
    
    
    
    def after_first_battle(self,Player1,Player2,):
        delay_print(f"\n{Player2}:pff...I knew you were weak..pathetic")
        delay_print(f"\n{Player2}:I'm out")
        delay_print(f"\n*{Player2} leaves*\n")
        delay_print(f"\n{Player1}:I should get stronger")
        while True:
            go_outside = input("\nEnter 'g' to go outside: \n")
            if go_outside == 'g':
                delay_print(f"\n*You go outside and stare at the long pathway to your first gym*\n")
                break
            else:
                delay_print("\nInvalid try again.")
        delay_print("More in full version....")






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
    
    Squirtle.introduce_game_with_storyline(Bulbasaur,'Ash','May')
    Squirtle.frist_fight(Bulbasaur,'Ash','May')
    Squirtle.after_first_battle('Ash','May')
