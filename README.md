# Smart Expense Analyzer — AI-Powered

Smart Expense Analyzer is an upgraded Python Expense Tracker that combines traditional expense management with machine learning and interactive financial analytics.

The application helps users record expenses, automatically categorize spending descriptions using a locally trained Machine Learning model, explore spending patterns, and identify potentially unusual transactions.

## Features

### Expense Management
- Add and save expenses
- View transaction history
- Search and filter transactions
- Delete transactions
- Export expense records to CSV
- Retain the original command-line interface

### AI-Powered Categorization
- Automatically predicts expense categories from descriptions
- Uses TF-IDF text vectorization and a Linear Support Vector Machine (Linear SVM)
- Supports seven expense categories:
  - Bills
  - Education
  - Entertainment
  - Food
  - Health
  - Shopping
  - Transport
- Saves the trained model locally using Joblib

### Financial Analytics
- Total spending and transaction statistics
- Category-wise spending breakdown
- Monthly spending trends
- Average expense analysis
- Rule-based unusual expense detection

### Interactive Dashboard
- Streamlit-based interface
- Interactive charts
- AI expense prediction
- Manual expense entry
- Transaction management and CSV export

## Machine Learning

The categorization model uses a text-classification pipeline:

1. Expense descriptions are converted into numerical features using TF-IDF.
2. Unigrams and bigrams are extracted.
3. A Linear SVM classifier predicts the expense category.
4. The trained pipeline is saved as a Joblib model.

### Dataset

- 345 curated and synthetic expense-description examples
- 7 expense categories
- Dataset file: `data/expense_training_data.csv`

The dataset is intended for a learning and portfolio project. Its performance should not be interpreted as a guarantee of accuracy on all real-world expense descriptions.

### Model Evaluation

The models were compared using 5-fold stratified cross-validation.

| Model | Accuracy | Macro F1 |
|---|---:|---:|
| Linear SVM | 88.41% | 88.25% |
| Complement Naive Bayes | 87.83% | 87.44% |
| Logistic Regression | 83.19% | 82.90% |

Linear SVM was selected as the final model.

An independent 20% holdout evaluation of the selected model produced:

- Test examples: 69
- Accuracy: 85.51%
- Macro F1: 85.12%

These results are based on the curated dataset and may differ on unseen real-world data.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Linear SVM
- Joblib
- Streamlit
- Plotly
- Matplotlib
- CSV

## Project Structure

```text
Python-Expense-Tracker/
├── data/
│   ├── expense_training_data.csv
├── models/
│   └── expense_category_model.joblib
├── analytics.py
├── app.py
├── expense_manager.py
├── main.py
├── ml_categorizer.py
├── storage.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/mateenshabbir910-blip/Python-Expense-Tracker.git
cd Python-Expense-Tracker
```

Create and activate a virtual environment.

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

## Run the Application

Start the dashboard:
```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

Run the CLI application:
```bash
python main.py
```

## Train the Model
```bash
python ml_categorizer.py
```

## Evaluate the Model
```bash
python compare_models.py
python validate_best_model.py
```

## Data and Privacy

Expense records are stored locally in data/expenses.csv. Personal transaction data should not be uploaded to a public repository.

The categorization model runs locally and does not require a paid AI API.

The training dataset contains curated and synthetic examples. Results may differ on real-world expense descriptions.

## Future Improvements

- Calibrated prediction confidence
- More robust anomaly detection
- Budget planning and spending alerts
- Database integration

## Author

Mateen

GitHub: https://github.com/mateenshabbir910-blip
