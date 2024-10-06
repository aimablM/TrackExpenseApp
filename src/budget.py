import uuid


def generate_unique_id():
    return str(uuid.uuid4())


class Budget:
    def __init__(self, user_id, category_id, amount, start_date, end_date):
        self.budget_id = generate_unique_id()
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date
        self.current_spending = 0.0
