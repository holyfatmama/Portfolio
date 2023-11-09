import os

from cs50 import SQL
from flask import render_template, redirect, Flask, request

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
        importance = request.form.get("importance")
        deadline = request.form.get("deadline")
        if not importance:
            importance = 0

    db.execute("INSERT INTO tasks ())


    return render_template("addtask.html")
