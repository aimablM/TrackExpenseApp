import uuid
from hashlib import sha256
from datetime import datetime
from expense import Expense


def generate_unique_id():
    return str(uuid.uuid4())


def encrypt_password(password):
    return sha256(password.encode()).hexdigest()


def save_user(self):
    print(f"User {self.username} created successfully!")


class User:

    def __init__(
        self, username, password, email, first_name, last_name, dob, user_id=None
    ):
        self.user_id = user_id if user_id else generate_unique_id()
        self.username = username
        self.password = encrypt_password(password)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.registration_date = datetime.now()
        # self.budget = None
        # self.expense = []

        save_user(self)

    def register(self, username, password, email, first_name, last_name, dob):
        # Logic to save user details to database
        self.username = username
        self.password = encrypt_password(password)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def login(self, username, password):
        try:
            if self.username == username and self.password == encrypt_password(
                password
            ):
                print("Login Successful!")
                return True
            else:
                raise ValueError(
                    "Login failed. Please check your username and password."
                )
                return False
        except Exception as e:
            print(f"Login failed: {e}")
            return False

    def add_expense(self, name, category, amount, description):
        expense = Expense(self.user_id, name, category, amount, description)
        self.expense.append(expense)
        print(f"{name} added to {self.first_name} expenses")

    def delete_expense(self):
        pass

    def create_budget():
        # Budget code to be implemented
        pass

    def display_info(self):
        print(
            f"Name: {self.first_name + " " + self.last_name} Email: {self.email} Username: {self.username}, DOB: {self.dob} Account Created: {self.registration_date}"
        )
