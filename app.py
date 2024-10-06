from flask import Flask, render_template, request, redirect, url_for, session
from src.user import User, encrypt_password

app = Flask(__name__)

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
            return redirect(url_for("index"))
        else:
            return "Login Failed. Check your username and password."
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
