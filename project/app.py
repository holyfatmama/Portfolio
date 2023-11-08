import os

from cs50 import SQL
from flask import render_template, redirect, Flask

app = Flask(__name__)

db = SQL("sqlite:///tasks.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addtask", methods=["GET", "POST"])
def addtask():
    if request.method == "POST":

        # flash added message after adding it in
        return render_template("index.html")

    else:
        return render_template("addtask.html")
