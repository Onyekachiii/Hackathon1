import time #for the time pause
import numpy as np
import sys
import json # load json file
import random #for random randint
import psycopg2


# Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, pokemon):
        self.effect(pokemon)

def heal_20(pokemon):
    pokemon.heal(20)

def heal_50(pokemon):
    pokemon.heal(50)

potion = Item("Potion", "Restores 20 health points.", heal_20)
super_potion = Item("Super Potion", "Restores 50 health points.", heal_50)



class Pokemon:
    def __init__(self, name, types, moves, EVs, description, health='====================', height='', weight=''):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20
        self.inventory = []
        self.description = description
        self.height = height
        self.weight = weight
    
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
        delay_print("Legend has it that Arconia possesses immense power to protect the Pokémon world.")
        delay_print("But it is under threat from the evil Team Darkstorm.")
        delay_print("You must gather the strongest Pokémon and defeat Team Darkstorm to save Arconia.")
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
        while True:
            give_nickname = input(f"\nDo you wish to give {self.name} a nickname? (Yes/No): ")

            if give_nickname.lower() == 'yes':
                while True:
                    self.new_name = input(f"\nWhat nickname do you want to give your {self.name}?: ")
                    confirm_nickname = input(f"\nAre you sure you want {self.name} to be nicknamed as {self.new_name}? (Yes/No): ")

                    if confirm_nickname.lower() == 'yes':
                        delay_print(f"\n{self.name} is now named {self.new_name}")
                        break
                    else:
                        # Ask for the nickname again
                        continue
                # Exit the outer loop as the nickname confirmation process is complete
                break
            else:
                self.new_name = self.name
                break




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
    
    def use_item(self, item):
        item.effect(self)

    def heal(self, amount):
        self.health = '=' * (len(self.health) + amount)
        if len(self.health) > 20:
            self.health = '=' * 20
    
    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        delay_print("\nInventory:")
        for i, item in enumerate(self.inventory):
            delay_print(f"{i + 1}. {item.name}: {item.description}")

    def choose_item(self):
        try:
            item_choice = int(input("\nEnter the number of the item you want to use: ")) - 1
            selected_item = self.inventory[item_choice]
            return selected_item
        except (IndexError, ValueError):
            return None
    
    
    
    
    def frist_fight(self, Pokemon2, Player1, Player2):
        delay_print(f"{Player2}:{Player1}, I challenge you to a pokemon battle\n")
        delay_print("\n~~~~POKEMON BATTLE~~~~~\n")
        delay_print(f"\n{self.new_name}")
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
        active_pokemon = self
        available_pokemon = [self]
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
            while True:
                delay_print(f"\nWhat are you going to do:'1.Fight','2.Use item','3.Switch pokemon','4.Run'")
                decision = input("\nEnter: ")
                if decision == '1':
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
                    break
                elif decision == '4':
                    delay_print("Pokemon trainers battle.Unable to run")
                elif decision == '3':
                    if len(available_pokemon) == 1:
                        delay_print("You only have one Pokémon!")
                    else:
                        delay_print("\nChoose a Pokémon to switch to:")
                        for i, pokemon in enumerate(available_pokemon):
                            delay_print(f"{i + 1}. {pokemon.name}")
                        try:
                            switch_choice = int(input("\nEnter the number of the Pokémon you want to switch to: ")) - 1
                            active_pokemon = available_pokemon[switch_choice]
                            delay_print(f"{Player1} switched to {active_pokemon.name}!")
                        except (IndexError, ValueError):
                            delay_print("Invalid input. Please pick a valid Pokémon.")
                elif decision == "2":
                    if len(self.inventory) == 0:
                        delay_print("You don't have any items in your inventory.")
                    else:
                        self.show_inventory()
                        selected_item = self.choose_item()
                        if selected_item:
                            self.use_item(selected_item)
                            delay_print(f"\n{self.name} used {selected_item.name}!")
                        else:
                            delay_print("Invalid. Try again")
            
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
            # AI Opponent's turn
            ai_move_choice = random.randint(0, len(Pokemon2.moves) - 1)
            ai_selected_move = Pokemon2.moves[ai_move_choice]
            delay_print(f"\n{Player2}: {Pokemon2.name} used {ai_selected_move}")

            # Determine effectiveness for AI Opponent's move
            if player1_type in type_advantages:
                if player2_type in type_advantages[player1_type]:
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
        delay_print(f"\n{Player2}:pff...whatever")
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
        while True:
            delay_print("\nWhat do you want to do:\n1.Run around in bushes\n2.follow the path to gym\n3.Open old map\n4.Open pokedex\n5.Go to the nearest Pokemon Center\n6.Go to the nearest PokeMart\n7.Save\n8.Exit ")
            action = input("\nEnter here: ")
            if action == '1' or action == '2' or action == '3' or action == '5' or action == '6' or action == '7':
                delay_print('\nGet full version..')
            elif action == "4":
                while True:
                    delay_print("\nWhat would you like to do with your Pokédex?\n1.View Pokédex\n2.Exit")
                    pokedex_action = input("\nEnter your choice: ")

                    if pokedex_action == '1':
                        delay_print("\nViewing Pokédex...\n")
                        delay_print("\n=== Pokédex ===\n")
                        for pokemon_name, data in pokemon_data.items():
                            delay_print(f"\n{pokemon_name}:\nType: {data['types']}\nAttack: {data['EVs']['ATTACK']}\nDefense: {data['EVs']['DEFENSE']}\nDescription: {data['description']}\nHeight: {data['height']}\nWeight: {data['weight']}\n")
                            delay_print("\n-----------------\n")
                        delay_print("\n================\n")
                    elif pokedex_action == '2':
                        break  # Exit the Pokédex menu
                    else:
                        delay_print("\nInvalid option. Please try again.")
            elif action == "8":
                delay_print('\nGoodBye..')
                break
            else:
                delay_print("\nInvalid.Try")





if __name__ == '__main__':
    with open('pokemon_data.json', 'r') as f:
        pokemon_data = json.load(f)


    Charmander = Pokemon(**pokemon_data["Charmander"])
    Squirtle = Pokemon(**pokemon_data["Squirtle"])
    Bulbasaur = Pokemon(**pokemon_data["Bulbasaur"])
    
    try:
        db_name = {
            "hostname" : 'localhost',
            "username" : 'postgres',
            "password" : 'Splendour01%',
            "database" : 'Pokemon'   
    
        }
    # Establish PostgreSQL connection
        conn = psycopg2.connect(**db_name)
        cursor = conn.cursor()

        # Add your PostgreSQL code here
        cursor.execute("SELECT * FROM players LIMIT 30;")
        results = cursor.fetchall()
        print(results)

        # Commit changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()
    
    except psycopg2.Error as e:
        print("Error:", e)
    
    Charmander.introduce_game_with_storyline(Squirtle,'Ash','May')
    Charmander.frist_fight(Squirtle,'Ash','May')
    Charmander.after_first_battle('Ash','May')
