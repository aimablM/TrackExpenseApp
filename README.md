# TrackXpense

Welcome to the **TrackXpense**, a personal finance tracker! This project is designed to help users manage their expenses, set budgets, and visualize their financial data with ease. Whether you're a developer looking to expand your portfolio or someone who wants to better manage their personal finances, this project is a great place to start.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Classes and Interactions](#classes-and-interactions)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The **TrackXpense** is a Python-based application designed to help users track their expenses, set budgets, and visualize their spending habits. The project demonstrates the use of various Python libraries and best practices in coding and design.

## Features

- User Registration and Login
- Add, Edit, Delete, and View Expenses
- Create, Edit, Delete, and View Categories
- Set and Manage Budgets
- Generate and Export Financial Reports
- Visualize Data with Charts and Graphs

## Installation

To get started with the **TrackXpense**, follow these steps:

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/your-username/personal-finance-tracker.git
   cd personal-finance-tracker
   ```

2. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```sh
   python main.py
   ```

## Usage

1. **Register:** Create a new account by providing a username, password, email, and other details.
2. **Login:** Log in to your account using your credentials.
3. **Add Expenses:** Add expenses with details like date, category, amount, and description.
4. **Set Budgets:** Set budgets for different categories and track your spending.
5. **View Reports:** Generate and view financial reports.
6. **Visualize Data:** Visualize your expenses and budgets using charts and graphs.

## Classes and Interactions

### User Class

- **Attributes:** User ID, Username, Password, Email, First Name, Last Name, Date of Birth, Registration Date, Profile Picture URL, Expenses, Budget
- **Methods:** Register, Login, Logout, View Profile, Update Profile, Change Password, Add Expense, Set Budget

### Expense Class

- **Attributes:** Expense ID, User ID, Date, Category, Amount, Description, Currency
- **Methods:** Add Expense, Edit Expense, Delete Expense, View Expense

### Category Class

- **Attributes:** Category ID, User ID, Name, Description
- **Methods:** Add Category, Edit Category, Delete Category, View Category

### Budget Class

- **Attributes:** Budget ID, User ID, Category ID, Amount, Start Date, End Date, Current Spending
- **Methods:** Set Budget, View Budget, Edit Budget, Track Spending

### Report Class

- **Attributes:** Report ID, User ID, Start Date, End Date, Expense Data, Budget Data
- **Methods:** Generate Report, Visualize Data, Export Report

### Visualization Class

- **Attributes:** Visualization ID, User ID, Data, Chart Type
- **Methods:** Create Bar Chart, Create Pie Chart, Create Line Chart, Display Chart

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request or open an issue.

## License

---

## Contact

For any questions or inquiries, please contact:

- **Aimable Mugwaneza**
- **aimable.mugwaneza@gmail.com**
- **GitHub:** [aimablM](https://github.com/aimablM)

---
