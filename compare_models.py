import pandas as pd

from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import ComplementNB

df = pd.read_csv("data/expense_training_data.csv")

X = df["description"]
y = df["category"]

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

models = {
    "Logistic Regression": Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LogisticRegression(max_iter=2000, C=1.0))
    ]),

    "Linear SVM": Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LinearSVC(C=1.0))
    ]),

    "Complement Naive Bayes": Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", ComplementNB(alpha=0.5))
    ])
}

results = []

for name, model in models.items():
    scores = cross_validate(
        model,
        X,
        y,
        cv=cv,
        scoring=["accuracy", "f1_macro"],
        n_jobs=-1
    )

    results.append({
        "Model": name,
        "Accuracy": round(scores["test_accuracy"].mean(), 4),
        "Macro F1": round(scores["test_f1_macro"].mean(), 4)
    })

result_df = pd.DataFrame(results)
result_df = result_df.sort_values(
    by="Macro F1",
    ascending=False
)

print("\n========== MODEL COMPARISON ==========")
print(result_df.to_string(index=False))
