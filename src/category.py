import uuid


def generate_unique_id():
    return str(uuid.uuid4())


class Category:
    def __init__(self, name, description=""):
        self.category_id = generate_unique_id()
        # self.user_id = user_id
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Category: {self.name}, Description: {self.description}")

    def add_category(self, name, description):
        Category = Category(name, description)
        predefined_categories.append(Category)


predefined_categories = [
    Category("Gas", "Gas spending"),
    Category("Groceries", "Food and household items"),
    Category("Rent", "Monthly rent or mortgage payments"),
    Category("Utilities", "Electricity, water, internet, etc."),
    Category("Transportation", "Public transportation or ride services"),
    Category("Dining Out", "Restaurants and takeout"),
    Category("Entertainment", "Movies, concerts, and leisure activities"),
    Category("Health", "Medical bills, prescriptions, and insurance"),
    Category("Fitness", "Gym memberships or sports activities"),
    Category("Insurance", "Car, home, health insurance premiums"),
    Category("Education", "Tuition, books, and educational tools"),
    Category("Clothing", "Apparel and accessories"),
    Category("Travel", "Vacation and trip-related expenses"),
    Category("Subscriptions", "Recurring digital services like Netflix, Spotify"),
    Category("Gifts", "Presents and charitable donations"),
    Category("Savings", "Money set aside for savings or investments"),
]


def run_tests():
    category = Category("user123", "Gas", "Gas spending")

    category.display_info()
    print("ID: " + category.category_id)
    assert category.user_id == "user123"
    assert category.name == "Gas"
    assert category.description == "Gas spending"
    print("All tests passed")


if __name__ == "__main__":
    # run_tests()
    print(predefined_categories)
    Category.add_category("Food", "Eating out expenses")
    print("\n" + predefined_categories)
