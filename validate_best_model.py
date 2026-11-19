import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix
)

df = pd.read_csv("data/expense_training_data.csv")

X = df["description"]
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LinearSVC(C=1.0))
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\n========== INDEPENDENT TEST RESULTS ==========")
print("Training examples:", len(X_train))
print("Testing examples:", len(X_test))

print("\nAccuracy:", round(accuracy_score(y_test, predictions) * 100, 2), "%")
print("Macro F1:", round(f1_score(y_test, predictions, average="macro") * 100, 2), "%")

print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(y_test, predictions, zero_division=0))

print("\n========== CONFUSION MATRIX ==========")
print(confusion_matrix(y_test, predictions))

print("\n========== SAMPLE PREDICTIONS ==========")
for description, actual, predicted in zip(
    X_test.head(10),
    y_test.head(10),
    predictions[:10]
):
    print(f"{description} | Actual: {actual} | Predicted: {predicted}")
