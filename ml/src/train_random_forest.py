import joblib
from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

ML_DIR = Path(__file__).resolve().parents[1]
MODELS_DIR = ML_DIR / "models"
RESULTS_DIR = ML_DIR / "results"

# Load the same train-test split
split_path = MODELS_DIR / "train_test_text_split.joblib"
data = joblib.load(split_path)

X_train_text = data["X_train"]
X_test_text = data["X_test"]
y_train = data["y_train"]
y_test = data["y_test"]

print("Training samples:", len(X_train_text))
print("Testing samples:", len(X_test_text))

# Create the Random Forest pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    (
        "classifier",
        RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            class_weight="balanced_subsample",
            n_jobs=-1,
        ),
    ),
])

print("\nTraining Random Forest...")
pipeline.fit(X_train_text, y_train)

print("Random Forest training completed!")

# Evaluate the model
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

# Save results
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

results_path = RESULTS_DIR / "random_forest_corrected.txt"

with open(results_path, "w", encoding="utf-8") as file:
    file.write("Random Forest - Corrected Pipeline Results\n")
    file.write("=" * 44 + "\n")
    file.write(f"Training samples: {len(X_train_text)}\n")
    file.write(f"Testing samples: {len(X_test_text)}\n")
    file.write(f"Accuracy: {accuracy:.4f}\n\n")
    file.write("Confusion Matrix:\n")
    file.write(str(cm) + "\n\n")
    file.write("Classification Report:\n")
    file.write(report)

# Save the complete pipeline
model_path = MODELS_DIR / "random_forest_pipeline.joblib"
joblib.dump(pipeline, model_path)

print("\nResults saved at:", results_path)
print("Complete pipeline saved at:", model_path)
