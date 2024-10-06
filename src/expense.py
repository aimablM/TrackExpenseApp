import uuid
from datetime import datetime


def generate_unique_id():
    return str(uuid.uuid4())


class Expense:
    def __init__(self, user_id, name, category, amount, description, date=None):

        self.expense_id = generate_unique_id()
        self.user_id = user_id
        self.name = name
        self.category = category
        self.amount = amount
        self.description = description
        self.date = datetime.now()

    def display_info(self):
        print(
            f"Name: {self.name} Amount: {self.amount} Category: {self.category}, Description: {self.description} Date: {self.date}"
        )


def run_tests():
    expense = Expense("user123", "Milk", "Groceries", 100.0, "Weekly grocery shopping")

    expense.display_info()
    assert expense.user_id == "user123"
    assert expense.category == "Groceries"
    assert expense.amount == 100.0
    assert expense.description == "Weekly grocery shopping"
    assert isinstance(expense.date, datetime)
    print("Expense creation test passed.")


if __name__ == "__main__":
    run_tests()
    print("All tests passed!")
