from collections import defaultdict
from statistics import mean


def spending_overview(expenses):
    if not expenses:
        return {
            "total": 0,
            "count": 0,
            "average": 0,
            "highest_category": None
        }

    total = sum(float(item["amount"]) for item in expenses)

    category_totals = defaultdict(float)

    for item in expenses:
        category_totals[item["category"]] += float(item["amount"])

    highest_category = max(
        category_totals,
        key=category_totals.get
    )

    return {
        "total": round(total, 2),
        "count": len(expenses),
        "average": round(mean(float(item["amount"]) for item in expenses), 2),
        "highest_category": highest_category
    }


def category_breakdown(expenses):
    totals = defaultdict(float)

    for item in expenses:
        totals[item["category"]] += float(item["amount"])

    return {
        category: round(amount, 2)
        for category, amount in sorted(
            totals.items(),
            key=lambda item: item[1],
            reverse=True
        )
    }


def monthly_breakdown(expenses):
    totals = defaultdict(float)

    for item in expenses:
        month = item["date"][:7]
        totals[month] += float(item["amount"])

    return {
        month: round(amount, 2)
        for month, amount in sorted(totals.items())
    }


def detect_unusual_expenses(expenses):
    if len(expenses) < 2:
        return []

    amounts = [float(item["amount"]) for item in expenses]
    average = mean(amounts)

    # Initial rule-based anomaly detection
    threshold = average * 2

    return [
        item for item in expenses
        if float(item["amount"]) > threshold
    ]
