from datetime import datetime


def create_expense(amount, category, description):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if not category.strip():
        raise ValueError("Category cannot be empty.")

    if not description.strip():
        raise ValueError("Description cannot be empty.")

    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": round(float(amount), 2),
        "category": category.strip().title(),
        "description": description.strip()
    }


def calculate_total(expenses):
    return round(sum(expense["amount"] for expense in expenses), 2)


def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    return {
        category: round(amount, 2)
        for category, amount in summary.items()
    }


def monthly_summary(expenses, month):
    return round(
        sum(
            expense["amount"]
            for expense in expenses
            if expense["date"].startswith(month)
        ),
        2
    )
