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
        task = request.form.get("task")
        detail = request.form.get("detail")

    return render_template("addtask.html")
