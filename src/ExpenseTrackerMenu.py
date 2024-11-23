from datetime import datetime
from user import User
from expense import Expense
from category import Category, predefined_categories
from budget import Budget
from report import Report
from visualization import Visualization
from userRepo import UserRepo
from expenseRepo import ExpenseRepo


def clear_screen():
    """Clear the console screen"""
    print("\n" * 50)


def print_menu(title, options):
    """Generic menu printer"""
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    print("=" * 50)


def get_valid_input(prompt, validation_func=None, error_message=None):
    """Get and validate user input"""
    while True:
        user_input = input(prompt)
        if validation_func is None or validation_func(user_input):
            return user_input
        print(error_message or "Invalid input. Please try again.")


class ExpenseTrackerMenu:
    def __init__(self):
        self.user = None
        self.running = True
        self.user_repo = UserRepo("expense_tracker.db")
        self.expense_repo = ExpenseRepo("expense_tracker.db")
        self.current_user = None
        self.current_user_id = None
        self.logged_in = False

    def register_user(self):
        """Handle user registration"""
        print("\nUser Registration")
        print("-" * 20)
        username = get_valid_input("Enter username: ")
        password = get_valid_input("Enter password: ")
        email = get_valid_input("Enter email: ")
        first_name = get_valid_input("Enter first name: ")
        last_name = get_valid_input("Enter last name: ")
        dob = get_valid_input("Enter date of birth (YYYY-MM-DD): ")

        user = User(username, password, email, first_name, last_name, dob)
        self.user_repo.addUser(user)
        print("\nRegistration successful!")

    def login(self):
        """Handle user login"""
        print("\nUser Login")
        print("-" * 20)
        username = input("Username: ")
        password = input("Password: ")
        self.current_user = self.user_repo.authenticateUser(username, password)

        if self.current_user:
            self.current_user_id = self.current_user.user_id
            print(
                f"Login Successful {self.current_user.first_name}, ID: {self.current_user_id} !"
            )
            self.logged_in = True
            return True
        else:
            print("Login failed. Please check your username and password.")
            return False

    def add_expense(self):
        """Handle adding new expense"""
        print("\nAdd New Expense")
        print("-" * 20)

        # Show available categories
        print("\nAvailable Categories:")
        for idx, category in enumerate(predefined_categories, 1):
            print(f"{idx}. {category.name}")

        cat_idx = int(
            get_valid_input(
                "Select category (number): ",
                lambda x: x.isdigit() and 1 <= int(x) <= len(predefined_categories),
            )
        )
        category = predefined_categories[cat_idx - 1]

        name = get_valid_input("Enter expense name: ")
        amount = float(
            get_valid_input(
                "Enter amount: $", lambda x: x.replace(".", "", 1).isdigit()
            )
        )
        description = get_valid_input("Enter description: ")

        expense = Expense(
            self.current_user_id, name, category.name, amount, description
        )
        self.expense_repo.add_expense(expense)

        print("\nExpense added successfully!")
        self.logged_in_menu()

    def view_expenses(self):
        """Display all expenses"""

        current_user_expenses = self.expense_repo.get_expenses(self.current_user_id)

        if not current_user_expenses:
            print("\nNo expenses recorded yet.")
            return

        print("\nYour Expenses")
        print("-" * 60)
        print(f"{'Name':<15} {'Category':<15} {'Amount':<10} {'Description':<20}")
        print("-" * 60)

        for expense in current_user_expenses:
            print(
                f"{expense.name:<15} {expense.category:<15} ${expense.amount:<9.2f} {expense.description:<20}"
            )
        print("-" * 60)

    def visualize_expenses(self):
        """Create visualizations of expenses"""
        if not self.user.expense:
            print("\nNo expenses to visualize.")
            return

        # Aggregate expenses by category
        expenses_by_category = {}
        for expense in self.user.expense:
            if expense.category in expenses_by_category:
                expenses_by_category[expense.category] += expense.amount
            else:
                expenses_by_category[expense.category] = expense.amount

        vis = Visualization(expenses_by_category)

        while True:
            print_menu(
                "Visualization Options",
                ["Bar Chart", "Pie Chart", "Line Chart", "Return to Main Menu"],
            )

            choice = get_valid_input("Select option: ", lambda x: x in "1234")

            if choice == "1":
                vis.create_bar_chart("Expenses by Category")
            elif choice == "2":
                vis.create_pie_chart("Expense Distribution")
            elif choice == "3":
                vis.create_line_chart("Expense Trend")
            else:
                break

    def logged_in_menu(self):
        while self.logged_in:
            try:
                print_menu(
                    f"Welcome, {self.current_user.first_name}!",
                    [
                        "Add Expense",
                        "View Expenses",
                        "Visualize Expenses",
                        "Logout",
                        "Exit",
                    ],
                )
                choice = get_valid_input("Select option: ", lambda x: x in "12345")

                if choice == "1":
                    self.add_expense()
                elif choice == "2":
                    self.view_expenses()
                elif choice == "3":
                    self.visualize_expenses()
                elif choice == "4":
                    self.user = None
                    self.logged_in = False
                    print("\nLogged out successfully!")
                else:
                    self.running = False
                    print("\nThank you for using Expense Tracker!")
                    break
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

    def main_menu(self):
        """Main menu loop"""
        while self.running:
            if not self.user:
                print_menu("Expense Tracker", ["Register", "Login", "Exit"])

                choice = get_valid_input("Select option: ", lambda x: x in "123")

                if choice == "1":
                    self.register_user()
                elif choice == "2":
                    if self.login():
                        self.logged_in_menu()
                    else:
                        print("\nLogin failed. Please try again.")
                else:
                    self.running = False
                    print("\nThank you for using Expense Tracker!")


def main():
    menu = ExpenseTrackerMenu()
    menu.main_menu()


if __name__ == "__main__":
    main()
