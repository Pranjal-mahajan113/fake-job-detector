
import joblib
from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

ML_DIR = Path(__file__).resolve().parents[1]
MODELS_DIR = ML_DIR / "models"
RESULTS_DIR = ML_DIR / "results"

# Load the same train-test split used by the baseline model
split_path = MODELS_DIR / "train_test_text_split.joblib"
data = joblib.load(split_path)

X_train_text = data["X_train"]
X_test_text = data["X_test"]
y_train = data["y_train"]
y_test = data["y_test"]

print("Training samples:", len(X_train_text))
print("Testing samples:", len(X_test_text))

# Create the balanced Logistic Regression pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
        ),
    ),
])

# Train only on training text
pipeline.fit(X_train_text, y_train)

print("\nBalanced Logistic Regression training completed!")

# Evaluate on unseen testing text
y_pred = pipeline.predict(X_test_text)

accuracy = accuracy_score(y_test, y_pred)

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=[0, 1],
)

report = classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Real (0)", "Fake (1)"],
    zero_division=0,
)

print("\nAccuracy:", round(accuracy, 4))
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(report)

# Save results separately
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

results_path = RESULTS_DIR / "logistic_regression_balanced_corrected.txt"

with open(results_path, "w", encoding="utf-8") as file:
    file.write("Balanced Logistic Regression - Corrected Pipeline Results\n")
    file.write("=" * 60 + "\n")
    file.write(f"Training samples: {len(X_train_text)}\n")
    file.write(f"Testing samples: {len(X_test_text)}\n")
    file.write(f"Accuracy: {accuracy:.4f}\n\n")
    file.write("Confusion Matrix:\n")
    file.write(str(cm) + "\n\n")
    file.write("Classification Report:\n")
    file.write(report)

# Save the complete pipeline
model_path = MODELS_DIR / "logistic_regression_balanced_pipeline.joblib"
joblib.dump(pipeline, model_path)

print("\nResults saved at:", results_path)
print("Complete pipeline saved at:", model_path)
