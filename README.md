# Python Expense Tracker

A command-line based Expense Tracker built with Python. It allows users to record daily expenses, store them in a CSV file, and view useful spending summaries.

## Features

- Add expenses with amount, category, and description
- View all recorded expenses
- Calculate total expenses
- Generate category-wise spending summaries
- Generate monthly expense summaries
- Validate user input
- Store data persistently using CSV

## Technologies Used

- Python 3
- CSV
- Built-in Python modules

## Project Structure

    Python-Expense-Tracker/
    ├── data/
    │   └── expenses.csv
    ├── expense_manager.py
    ├── main.py
    ├── storage.py
    ├── README.md
    └── .gitignore

## Requirements

- Python 3.10 or later
- No external packages required

## How to Run

Run this command inside the project directory:

    python3 main.py

## Menu Options

1. Add Expense
2. View All Expenses
3. View Total Expenses
4. Category-wise Summary
5. Monthly Summary
6. Exit

## Data Storage

Expenses are stored locally in data/expenses.csv. Previously saved expenses are automatically loaded when the application starts.

## Input Validation

- Rejects zero and negative amounts
- Rejects empty categories
- Rejects empty descriptions
- Validates monthly date format

## Author

Mateen
