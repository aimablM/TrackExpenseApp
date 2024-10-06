import uuid


def generate_unique_id():
    return str(uuid.uuid4())


class Category:
    def __init__(self, user_id, name, description=""):
        self.category_id = generate_unique_id()
        self.user_id = user_id
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Category: {self.name}, Description: {self.description}")


def run_tests():
    category = Category("user123", "Gas", "Gas spending")

    category.display_info()
    print("ID: " + category.category_id)
    assert category.user_id == "user123"
    assert category.name == "Gas"
    assert category.description == "Gas spending"
    print("All tests passed")


if __name__ == "__main__":
    run_tests()
    print("Tests completed")
