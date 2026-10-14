
import joblib
import pandas as pd
from scipy.sparse import load_npz
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# Load target labels
data_path = r"E:\fake-job-detector\ml\data\fake_job_postings_cleaned.csv"
df = pd.read_csv(data_path)
y = df["fraudulent"]

# Load TF-IDF features
matrix_path = r"E:\fake-job-detector\ml\models\tfidf_matrix.npz"
X = load_npz(matrix_path)

# Use the same train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Load trained models
models = {
    "Logistic Regression Baseline": joblib.load(
        r"E:\fake-job-detector\ml\models\logistic_regression_baseline.joblib"
    ),
    "Logistic Regression Balanced": joblib.load(
        r"E:\fake-job-detector\ml\models\logistic_regression_balanced.joblib"
    ),
    "Multinomial Naive Bayes": joblib.load(
        r"E:\fake-job-detector\ml\models\naive_bayes_model.joblib"
    )
}

print("All three models loaded successfully!")


# Evaluate each model
results = []

for model_name, model in models.items():
    y_pred = model.predict(X_test)

    results.append({
        "Model": model_name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Fake Precision": precision_score(
            y_test, y_pred, pos_label=1, zero_division=0
        ),
        "Fake Recall": recall_score(
            y_test, y_pred, pos_label=1, zero_division=0
        ),
        "Fake F1 Score": f1_score(
            y_test, y_pred, pos_label=1, zero_division=0
        )
    })

comparison_df = pd.DataFrame(results)

print("\nModel Comparison:")
print(comparison_df.round(4).to_string(index=False))



# Save comparison results
results_path = r"E:\fake-job-detector\ml\results\model_comparison.csv"

comparison_df.to_csv(results_path, index=False)

print("\nComparison saved at:", results_path)
