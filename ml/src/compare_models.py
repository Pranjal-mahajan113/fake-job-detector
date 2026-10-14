import joblib
import pandas as pd
from pathlib import Path

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

ML_DIR = Path(__file__).resolve().parents[1]
MODELS_DIR = ML_DIR / "models"
RESULTS_DIR = ML_DIR / "results"

# Load the fixed test data
split_path = MODELS_DIR / "train_test_text_split.joblib"
data = joblib.load(split_path)

X_test_text = data["X_test"]
y_test = data["y_test"]

# Model names and saved pipeline paths
model_files = {
    "Logistic Regression": (
        "logistic_regression_baseline_pipeline.joblib"
    ),
    "Balanced Logistic Regression": (
        "logistic_regression_balanced_pipeline.joblib"
    ),
    "Naive Bayes": "naive_bayes_pipeline.joblib",
    "Random Forest": "random_forest_pipeline.joblib",
}

results = []

for model_name, filename in model_files.items():
    model_path = MODELS_DIR / filename

    print(f"\nEvaluating: {model_name}")

    pipeline = joblib.load(model_path)
    y_pred = pipeline.predict(X_test_text)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test, y_pred, pos_label=1, zero_division=0
    )
    recall = recall_score(
        y_test, y_pred, pos_label=1, zero_division=0
    )
    f1 = f1_score(
        y_test, y_pred, pos_label=1, zero_division=0
    )

    tn, fp, fn, tp = confusion_matrix(
        y_test, y_pred, labels=[0, 1]
    ).ravel()

    results.append({
        "model": model_name,
        "accuracy": round(accuracy, 4),
        "fake_precision": round(precision, 4),
        "fake_recall": round(recall, 4),
        "fake_f1": round(f1, 4),
        "true_negatives": int(tn),
        "false_positives": int(fp),
        "false_negatives": int(fn),
        "true_positives": int(tp),
    })

comparison = pd.DataFrame(results)
comparison = comparison.sort_values(
    by="fake_f1", ascending=False
)

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

output_path = RESULTS_DIR / "model_comparison_corrected.csv"
comparison.to_csv(output_path, index=False)

print("\nFinal Model Comparison:")
print(comparison.to_string(index=False))

print("\nComparison saved at:", output_path)
