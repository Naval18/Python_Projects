import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO

def get_pokemon_data():
    pokemon = entry.get().lower().strip()
    if not pokemon:
        messagebox.showwarning("Input Error", "Please enter a Pokémon name!")
        return

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code != 200:
        messagebox.showerror("Error", "Pokémon not found! Please check the name.")
        return

    data = response.json()


    name = data["name"].title()
    pokemon_id = data["id"]
    types = ", ".join([t["type"]["name"] for t in data["types"]])
    base_experience = data["base_experience"]
    sprite_url = data["sprites"]["front_default"]


    info_label.config(
        text=f"Name: {name}\n"
             f"ID: {pokemon_id}\n"
             f"Type(s): {types}\n"
             f"Base XP: {base_experience}"
    )


    if sprite_url:
        img_response = requests.get(sprite_url)
        img_data = img_response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((120, 120))
        photo = ImageTk.PhotoImage(img)
        sprite_label.config(image=photo)
        sprite_label.image = photo
    else:
        sprite_label.config(image="", text="No Image Found")


root = tk.Tk()
root.title("Pokémon Info Viewer ⚡")
root.geometry("350x500")
root.config(bg="#FFF176")  # Pikachu yellow


title_label = tk.Label(
    root, text="Pokémon Info Viewer",
    bg="#FFF176", fg="#E65100",
    font=("Comic Sans MS", 18, "bold")
)
title_label.pack(pady=15)


entry = tk.Entry(
    root, width=25, bg="#FFF9C4", fg="#E65100",
    font=("Arial", 12), justify="center", relief="groove", bd=3
)
entry.pack(pady=8)


fetch_button = tk.Button(
    root, text="Get Info", command=get_pokemon_data,
    bg="#FFB300", fg="white", font=("Arial", 11, "bold"),
    relief="raised", activebackground="#F57F17", bd=4
)
fetch_button.pack(pady=10)


info_frame = tk.Frame(root, bg="#FFFDE7", bd=4, relief="ridge")
info_frame.pack(pady=10, fill="x", padx=15)


sprite_label = tk.Label(info_frame, bg="#FFFDE7")
sprite_label.pack(pady=10)


info_label = tk.Label(
    info_frame, text="", bg="#FFFDE7", fg="#5D4037",
    font=("Consolas", 10), justify="left"
)
info_label.pack(pady=5)


footer = tk.Label(
    root, text="Data from PokéAPI | Not affiliated with Nintendo",
    bg="#FFF176", fg="#6D4C41", font=("Arial", 8)
)
footer.pack(side="bottom", pady=10)

root.mainloop()
