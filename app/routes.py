from flask import render_template
import os, json
from app import app

@app.route("/")
def index():
    names = []
    files = os.listdir('pokeinfo/pokemons')     # array with the names of the pokemon files
    for archive in files:
        with open(f'pokeinfo/pokemons/{archive}') as f:
            pokemon = json.load(f)
            names.append(pokemon["name"])       # for each pokemon add its name to 'names' array

    return render_template("index.html", data=names)