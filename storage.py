import csv
import os

FILE_PATH = "data/expenses.csv"

FIELDNAMES = ["date", "amount", "category", "description"]


def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expenses = []

        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)

        return expenses


def save_expense(expense):
    os.makedirs("data", exist_ok=True)

    file_exists = os.path.exists(FILE_PATH)

    with open(FILE_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists or os.path.getsize(FILE_PATH) == 0:
            writer.writeheader()

        writer.writerow(expense)


def save_all_expenses(expenses):
    os.makedirs("data", exist_ok=True)

    with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)
