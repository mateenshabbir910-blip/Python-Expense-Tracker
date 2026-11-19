import pandas as pd

from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report
)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


DATA_PATH = "data/expense_training_data.csv"

data = pd.read_csv(DATA_PATH)

X = data["description"]
y = data["category"]

model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LogisticRegression(max_iter=1000))
])

cv = StratifiedKFold(
    n_splits=4,
    shuffle=True,
    random_state=42
)

predictions = cross_val_predict(model, X, y, cv=cv)

print("\n========== MODEL EVALUATION ==========")
print(f"Training examples: {len(data)}")
print(f"Categories: {y.nunique()}")
print(f"Cross-validation folds: 4")
print(f"Accuracy: {accuracy_score(y, predictions):.2%}")
print(f"Macro F1-score: {f1_score(y, predictions, average='macro'):.2%}")

print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(y, predictions, zero_division=0))
