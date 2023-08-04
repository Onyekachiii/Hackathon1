import pypokedex  # pokemon info
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3  # for links
from io import BytesIO  # to get pokemon links
import random

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.stats = 50
        self.hp = 50

def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get())

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))
    
    image = image.resize((100, 100))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=f"{', '.join(pokemon.types)}")
    update_base_stats(my_pokemon)
    pokemon_height.config(text=f"Height: {pokemon.height} inch")
    pokemon_weight.config(text=f"Weight: {pokemon.weight} kg")

def update_base_stats(pokemon_obj):
    base_stats_text = f"Base Stats: {pokemon_obj.base_stats}"
    if pokemon_obj.stats > 50:
        base_stats_text += f" (+{pokemon_obj.stats - 50})"
    pokemon_base_stats.config(text=base_stats_text)

def feed_pokemon():
    if my_pokemon:
        my_pokemon.stats += 10
        my_pokemon.hp += 10
        text_box.insert(tk.END, f"{my_pokemon.name} is fed and its stats and HP increased!\n")
        update_base_stats(my_pokemon)
    else:
        text_box.insert(tk.END, "No Pokémon to feed!\n")
    text_box.see(tk.END)

def delete_pokemon():
    global my_pokemon
    if my_pokemon:
        text_box.insert(tk.END, f"You released {my_pokemon.name}. It's now free!\n")
        my_pokemon = None
    else:
        text_box.insert(tk.END, "No Pokémon to release!\n")
    text_box.see(tk.END)

def catch_pokemon():
    global my_pokemon
    if my_pokemon:
        text_box.insert(tk.END, "You already have a Pokémon!\n")
    else:
        pokemon_names = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"]
        chosen_name = random.choice(pokemon_names)
        my_pokemon = Pokemon(chosen_name)
        text_box.insert(tk.END, f"You caught a {my_pokemon.name}!\n")
        text_box.insert(tk.END, f"Now you can feed, release, or catch more Pokémon.\n")
        update_base_stats(my_pokemon)
    text_box.see(tk.END)

def display_stats():
    if my_pokemon:
        text_box.insert(tk.END, f"{my_pokemon.name}'s stats: {my_pokemon.stats}\n")
    else:
        text_box.insert(tk.END, "No Pokémon to display stats for!\n")
    text_box.see(tk.END)

window = tk.Tk()
window.geometry("1000x800")
window.title("Pokemon Pokedex")
window.config(padx=5, pady=5, bg="light blue")

title_label = tk.Label(window, text="Pokemon Pokedex")
title_label.config(font=("Cursive", 32), bg="light blue")
title_label.pack(padx=5, pady=5)

pokemon_image = tk.Label(window)
pokemon_image.config(bg="light blue")
pokemon_image.pack(padx=5, pady=5)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Segoe UI", 20), bg="light blue")
pokemon_information.pack(padx=5, pady=5)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Segoe UI", 20), bg="light blue")
pokemon_types.pack(padx=5, pady=5)

pokemon_base_stats = tk.Label(window)
pokemon_base_stats.config(font=("Segoe UI", 20), bg="light blue")
pokemon_base_stats.pack(padx=5, pady=5)

pokemon_height = tk.Label(window)
pokemon_height.config(font=("Segoe UI", 20), bg="light blue")
pokemon_height.pack(padx=5, pady=5)

pokemon_weight = tk.Label(window)
pokemon_weight.config(font=("Segoe UI", 20), bg="light blue")
pokemon_weight.pack(padx=5, pady=5)

text_id_name = tk.Entry(window, font=("Segoe UI", 20), width=30)
text_id_name.pack(padx=5, pady=5)

btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Segoe UI", 20), bg="light blue", border=5)
btn_load.pack(padx=5, pady=5)
btn_load.config(height=0, width=15) 

btn_feed = tk.Button(window, text="Feed Pokemon", command=feed_pokemon)
btn_feed.config(font=("Segoe UI", 20), bg="light blue", border=5)
btn_feed.pack(padx=5, pady=5)
btn_feed.config(height=0, width=15) 

btn_delete = tk.Button(window, text="Delete Pokemon", command=delete_pokemon)
btn_delete.config(font=("Segoe UI", 20), bg="light blue", border=5)
btn_delete.pack(padx=5, pady=5)
btn_delete.config(height=0, width=15) 

btn_catch = tk.Button(window, text="Catch Pokemon", command=catch_pokemon)
btn_catch.config(font=("Segoe UI", 20), bg="light blue", border=5)
btn_catch.pack(padx=5, pady=5)
btn_catch.config(height=0, width=15)

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = tk.Text(window, height=3, width=30, yscrollcommand=scrollbar.set)
text_box.config(font=("Segoe UI", 14))
text_box.pack(padx=5, pady=5)
text_box.insert(tk.END, "Welcome to the Pokemon Mini Game!\n")
text_box.insert(tk.END, "Press '1' to catch a Pokémon.\n")
text_box.insert(tk.END, "Press '2' to feed your Pokémon.\n")
text_box.insert(tk.END, "Press '3' to release your Pokémon.\n")

my_pokemon = None  # Placeholder for the caught Pokémon

scrollbar.config(command=text_box.yview)

window.mainloop()
