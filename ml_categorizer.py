import pandas as pd
import joblib

from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

DATA_PATH = Path("data/expense_training_data.csv")
MODEL_PATH = Path("models/expense_category_model.joblib")


def train_model():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Training dataset not found: {DATA_PATH}"
        )

    data = pd.read_csv(DATA_PATH)

    if data.empty:
        raise ValueError("Training dataset is empty.")

    if data["description"].isna().any() or data["category"].isna().any():
        raise ValueError("Training dataset contains missing values.")

    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(ngram_range=(1, 2))
        ),
        (
            "classifier",
            LinearSVC(C=1.0)
        )
    ])

    model.fit(
        data["description"].astype(str),
        data["category"].astype(str)
    )

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("Linear SVM model trained successfully!")
    print(f"Training examples: {len(data)}")
    print(f"Categories: {sorted(data['category'].unique())}")
    print(f"Model saved at: {MODEL_PATH}")

    return model


def predict_category(description):
    if not str(description).strip():
        raise ValueError("Expense description cannot be empty.")

    if not MODEL_PATH.exists():
        raise FileNotFoundError("Train the model first.")

    model = joblib.load(MODEL_PATH)

    prediction = model.predict([description.strip()])

    return prediction[0]


if __name__ == "__main__":
    train_model()

    print("\nSample predictions:")

    test_expenses = [
        "Uber ride",
        "Lunch at restaurant",
        "Electricity bill",
        "Bought new shoes",
        "University fee",
        "Doctor appointment",
        "Netflix subscription"
    ]

    for expense in test_expenses:
        category = predict_category(expense)
        print(f"{expense} -> {category}")
