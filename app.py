# Imports
from flask import Flask, render_template


# Flask
app = Flask(__name__)


#Routes
@app.route("/")
def main():
    return render_template("index.html")
