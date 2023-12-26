import os

from cs50 import SQL
from flask import render_template, redirect, Flask, request, flash

app = Flask(__name__)

db = SQL("sqlite:///tasks.db")

@app.route("/", methods=["GET", "POST"])
def index():
    tasks = db.execute("SELECT * FROM tasks")
    if request.method == "POST":
        id = request.form.get("id")
        db.execute("DELETE FROM tasks WHERE id = ?", id)
        return redirect("/")
    else:
        return render_template("index.html", tasks = tasks)

@app.route("/addtask", methods=["GET", "POST"])
def addtask():
    tasks = db.execute("SELECT * FROM tasks")
    if request.method == "POST":
        task = request.form.get("task")
        detail = request.form.get("detail")
        importance = request.form.get("importance")
        deadline = request.form.get("deadline")
        if not importance:
            importance = 0
        db.execute("INSERT INTO tasks (task, detail, importance, deadline) VALUES (?, ?, ?, ?)", task, detail, importance, deadline)
        return redirect("/")
    else:
        return render_template("addtask.html", tasks = tasks)
