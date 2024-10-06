from user import User
from expense import Expense
from category import Category
from budget import Budget
from report import Report
from visualization import Visualization


def main():
    # Creation of user
    user = User(
        username="john_doe",
        password="securepassword123",
        email="john@example.com",
        first_name="John",
        last_name="Doe",
        dob="1990-01-01",
    )

    category = Category(user.user_id, "Food", "Eating out expenses")
    expense = Expense(
        user.user_id, "Chipotle", category.name, 50.0, "Tuesday Lunch", 2024 - 10 - 5
    )

    # Set budget
    budget = Budget(
        user.user_id, category.category_id, 500.0, "2024-01-01", "2024-01-31"
    )

    # Report
    expenses_data = {"Groceries": 150, "Entertainment": 100}
    budgets_data = {"Groceries": 200, "Entertainment": 150}
    report = Report(
        user.user_id, "2024-01-01", "2024-01-31", expenses_data, budgets_data
    )
    print(report.generate_report())

    # Visualize data
    vis = Visualization(expenses_data)
    vis.create_bar_chart("Monthly Expenses Bar Chart")


if __name__ == "__main__":
    main()
