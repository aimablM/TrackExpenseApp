from flask import Flask, render_template, request, redirect, url_for, session
from src.user import User, encrypt_password
from src.expense import Expense
from src.category import Category

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Needed to use sessions

# Placeholder for user storage
users = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        dob = request.form["dob"]
        user = User(username, password, email, first_name, last_name, dob)
        user.register(username, password, email, first_name, last_name, dob)
        users.append(user)
        print(users)  # Print the users array to confirm
        return redirect(url_for("index"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = next(
            (
                u
                for u in users
                if u.username == username and u.password == encrypt_password(password)
            ),
            None,
        )
        if user:
            session["username"] = user.username
            return redirect(url_for("home"))
        else:
            return "Login Failed. Check your username and password."
    return render_template("login.html")


@app.route("/home")
def home():
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))
    user = next((u for u in users if u.username == username), None)
    if not user:
        return "User not found."
    return render_template(
        "home.html",
        user=user,  # predefined_categories=predefined_categories
    )


@app.route("/add")
def add_expense():
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))
    user = next((u for u in users if u.username == username), None)
    if not user:
        return "User not found."
    return render_template(
        "home.html",
        user=user,  # predefined_categories=predefined_categories
    )


@app.route("/add_expense", methods=["POST"])
def add_expense():
    category_name = request.form["expense_category"]
    amount = float(request.form["expense_amount"])
    description = request.form["expense_description"]
    username = session.get("username")
    user = next((u for u in users if u.username == username), None)
    if user:
        category = next(
            (c for c in predefined_categories if c.name == category_name), None
        )
        if category:
            expense = Expense(user.user_id, category.name, amount, description)
            user.expenses.append(expense)
            return redirect(url_for("home"))
        else:
            return "Category not found."
    else:
        return "User not found."


if __name__ == "__main__":
    app.run(debug=True)
