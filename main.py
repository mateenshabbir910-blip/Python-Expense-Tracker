from expense_manager import (
    create_expense,
    calculate_total,
    category_summary,
    monthly_summary
)
from storage import load_expenses, save_expense


def display_menu():
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Category-wise Summary")
    print("5. Monthly Summary")
    print("6. Exit")
    print("=====================================")


def add_new_expense(expenses):
    try:
        amount = float(input("Enter amount (PKR): "))

        if amount <= 0:
            print("Invalid input: Amount must be greater than zero.")
            return

        category = input("Enter category: ")
        if not category.strip():
            print("Invalid input: Category cannot be empty.")
            return

        description = input("Enter description: ")
        if not description.strip():
            print("Invalid input: Description cannot be empty.")
            return

        expense = create_expense(amount, category, description)
        save_expense(expense)
        expenses.append(expense)

        print("Expense added successfully!")

    except ValueError as error:
        print(f"Invalid input: {error}")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n----------- ALL EXPENSES -----------")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['date']} | "
            f"PKR {expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


def show_total(expenses):
    print(f"Total Expenses: PKR {calculate_total(expenses):.2f}")


def show_category_summary(expenses):
    summary = category_summary(expenses)

    if not summary:
        print("No expenses available.")
        return

    print("\n------- CATEGORY SUMMARY -------")

    for category, amount in summary.items():
        print(f"{category}: PKR {amount:.2f}")


def show_monthly_summary(expenses):
    month = input("Enter month (YYYY-MM): ").strip()

    try:
        from datetime import datetime
        datetime.strptime(month, "%Y-%m")

        total = monthly_summary(expenses, month)
        print(f"Expenses for {month}: PKR {total:.2f}")

    except ValueError:
        print("Invalid month format. Use YYYY-MM.")


def main():
    expenses = load_expenses()
    print("Welcome to Python Expense Tracker!")

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_new_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_category_summary(expenses)
        elif choice == "5":
            show_monthly_summary(expenses)
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
