import os

from cs50 import SQL
from flask import render_template, redirect, Flask

app = Flask(__name__)

db = SQL("sqlite:///tasks.db")

@app.route("/")
def index():
    return render_template("index.html")
