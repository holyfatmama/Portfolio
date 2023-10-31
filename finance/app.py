import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # look thru each line of transaction by user, group the total/sum of symbol and present data
    return apology("ily")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Please input a symbol")

        if not shares:
            return apology("Please enter a correct amount")

        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("symbol not found")

        price = quote["price"]
        shares = request.form.get("shares")

        # select cash amount from database
        cash = db.execute("SELECT cash FROM users WHERE id = ?", request.form.get("username"))

        # check if there is enough cash, if it is, update cash amount, if not return apology
        total_cost = shares * price
        if cash < total_cost:
            return apology("not enough cash")

        rows = db.execute("SELECT * FORM users WHERE id = ?", session["user_id"])

        session["user_id"] = rows[0]["id"]

        db.execute("UPDATE users SET cash = (cash - ?) WHERE id = ?", total_cost, session["user_id"])


        return render_template("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # look through each line of transaction where ? equals to username and display it
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if not quote:
            return apology("Please enter correct symbol")
        return render_template("quote.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        hash = generate_password_hash(request.form.get("password"))

        # check if username is empty
        if not username:
            return apology("please enter username")

        # check if password is empty
        if not password:
            return apology("please enter password")

        # check if confirmation is empty
        if not confirmation:
            return apology("please enter confirmation")

        # check if confirmation is same as password
        if confirmation != password:
            return apology("please enter same password as confirmation")

        # check if database has username
        users = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(users) != 0:
            return apology ("username already exists")

        # insert username and hash into database
        db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hash)

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # remember session
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # render apology if fail to select a stock to sell

    # apology if fail to input amount

    # use <option> to select stocks owned by looking through database

    # lookup symbol to sell

    # update database by removing previously bought transaction and updating cash balance with the CURRENT price

    # POST action by selling
    return apology("TODO")
