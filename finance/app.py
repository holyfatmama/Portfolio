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
    # get user stocks
    stocks = db.execute(
        "SELECT symbol, SUM(shares) FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
        session["user_id"],
    )

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0][
        "cash"
    ]

    grand_total = cash

    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = quote["price"]
        stock["total_shares"] = stock["SUM(shares)"]
        stock["value"] = stock["price"] * stock["total_shares"]
        grand_total += stock["value"]

    return render_template(
        "index.html", stocks=stocks, cash=cash, grand_total=grand_total
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        if not symbol:
            return apology("Please input a symbol")
        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("Please enter a correct amount of shares")

        quote = lookup(symbol)
        if quote is None:
            return apology("symbol not found")

        price = quote["price"]
        total_cost = int(shares) * float(price)
        # select cash amount from database
        cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0][
            "cash"
        ]

        # check if there is enough cash, if it is, update cash amount, if not return apology
        if cash < total_cost:
            return apology("not enough cash")

        # execute buy to users table
        db.execute(
            "UPDATE users SET cash = (cash - ?) WHERE id = ?",
            total_cost,
            session["user_id"],
        )

        # insert transaction into transactions table
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
            session["user_id"],
            symbol,
            shares,
            price,
        )

        flash(f"Bought {shares} shares of {symbol} for {usd(total_cost)}!")

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # look through each line of transaction where ? equals to username and display it
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = ? ORDER BY timestamp DESC",
        session["user_id"],
    )

    return render_template("history.html", transactions=transactions)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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
        symbol = request.form.get("symbol").upper()
        quote = lookup(symbol)
        if not quote:
            return apology("Please enter correct symbol", 400)
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
            return apology("username already exists")

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
    stocks = db.execute(
        "SELECT symbol, SUM(shares) FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
        session["user_id"],
    )
    if request.method == "POST":
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0][
            "cash"
        ]

        shares = request.form.get("shares")
        symbol = request.form.get("symbol")

        # check if number of shares selected is positive number

        if not symbol:
            return apology("Please select correct stock to sell")
        elif int(float(shares)) <= 0 or not shares.isdigit() or not shares:
            return apology("Please input a correct amount")
        else:
            shares = int(shares)

        for stock in stocks:
            if symbol == stock["symbol"]:
                if shares > stock["SUM(shares)"]:
                    return apology("Please only enter amounts of shares you own")
                else:
                    quote = lookup(stock["symbol"])
                    if quote is None:
                        return apology("please enter correct symbol")
                    stock["total_value_sell"] = quote["price"] * shares
                    cash += stock["total_value_sell"]
                    db.execute(
                        "UPDATE users SET cash = ? WHERE id = ?",
                        cash,
                        session["user_id"],
                    )
                    db.execute(
                        "INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                        session["user_id"],
                        symbol,
                        -shares,
                        quote["price"],
                    )
                    flash(
                        f" Sold {shares} share(s) of {symbol} for USD $ {}!"
                    )
                    return redirect("/")

    else:
        return render_template("sell.html", stocks=stocks)


@app.route("/addcash", methods=["GET", "POST"])
def addcash():
    if request.method == "POST":
        amount = request.form.get("amount")
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0][
            "cash"
        ]
        newcash = float(amount) + cash

        if float(amount) <= 0:
            return apology("Please enter a correct amount")
        else:
            db.execute(
                "UPDATE users SET cash = ? WHERE id = ?", newcash, session["user_id"]
            )
            flash(f"Added {usd(float(amount))}!")
        return redirect("/")
    else:
        return render_template("addcash.html")
