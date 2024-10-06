import matplotlib.pyplot as plt


class Visualization:
    def __init__(self, data):
        self.data = data

    def create_bar_chart(self, title="Bar Chart"):
        categories = list(self.data.keys())
        amounts = list(self.data.values())
        plt.bar(categories, amounts)
        plt.xlabel("Categories")
        plt.ylabel("Amount")
        plt.title(title)
        plt.show()

    def create_pie_chart(self, title="Pie Chart"):
        labels = list(self.data.keys())
        sizes = list(self.data.values())
        plt.pie(sizes, labels=labels, autopct="%1.1f%%")
        plt.title(title)
        plt.show()

    def create_line_chart(self, title="Line Chart"):
        categories = list(self.data.keys())
        amounts = list(self.data.values())
        plt.plot(categories, amounts, marker="o")
        plt.xlabel("Categories")
        plt.ylabel("Amount")
        plt.title(title)
        plt.show()


# Basic test function
def run_tests():
    data = {"Groceries": 150, "Entertainment": 100, "Utilities": 200}

    vis = Visualization(data)

    # Test bar chart creation
    print("Displaying bar chart...")
    vis.create_bar_chart("Monthly Expenses Bar Chart")

    # Test pie chart creation
    print("Displaying pie chart...")
    vis.create_pie_chart("Monthly Expenses Pie Chart")

    # Test line chart creation
    print("Displaying line chart...")
    vis.create_line_chart("Monthly Expenses Line Chart")


if __name__ == "__main__":
    run_tests()
    print("Visualization tests completed.")
