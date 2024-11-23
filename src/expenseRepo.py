from databaseConnection import DatabaseConnection
from expense import Expense
import sqlite3


class ExpenseRepo:

    def __init__(self, database_name) -> None:
        self.db = DatabaseConnection.get_instance(database_name)
        self.cursor = self.db.cursor
        self.connection = self.db.connection
        self.current_user_id = None

    def add_expense(self, expense: Expense):
        try:
            self.cursor.execute(
                "INSERT INTO expenses (expense_id, user_id, name, category, amount, description, date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    expense.expense_id,
                    expense.user_id,
                    expense.name,
                    expense.category,
                    expense.amount,
                    expense.description,
                    expense.date,
                ),
            )
            self.db.connection.commit()
        except Exception as e:
            print(f"Error adding expense: {e}")

    def remove_expense(self, expense_id):
        self.cursor.execute("DELETE FROM expenses WHERE expense_id = ?", (expense_id,))
        self.db.connection.commit()

    def edit_expense(self, expense: Expense):
        self.cursor.execute(
            "UPDATE expenses SET name = ?, category = ?, amount = ?, description = ? WHERE expense_id = ?",
            (
                expense.name,
                expense.category,
                expense.amount,
                expense.description,
                expense.expense_id,
            ),
        )
        self.db.connection.commit()

    def get_expenses(self, user_id):
        try:
            if not user_id:
                raise ValueError("User ID is required to get expenses")

            self.cursor.execute("SELECT * FROM expenses WHERE user_id = ?", (user_id,))
            expense_records = self.cursor.fetchall()
            print(expense_records)
            expenses = []

            for record in expense_records:
                expense_item = Expense(
                    expense_id=record[0],
                    user_id=record[1],
                    name=record[2],
                    category=record[3],
                    amount=record[4],
                    description=record[5],
                    date=record[6],
                )
                expenses.append(expense_item)
                print(expense_item)
            return expenses

        except Exception as e:
            print(f"Error getting expenses: {e}")
            return []
