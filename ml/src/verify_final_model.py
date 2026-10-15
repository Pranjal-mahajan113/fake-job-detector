
import joblib
import numpy as np
from pathlib import Path
from sklearn.metrics import accuracy_score, confusion_matrix

# Project paths
ML_DIR = Path(__file__).resolve().parents[1]
MODELS_DIR = ML_DIR / "models"

# Saved test data load karo
split_path = MODELS_DIR / "train_test_text_split.joblib"
data = joblib.load(split_path)

X_test = data["X_test"]
y_test = data["y_test"]

# Final model artifact load karo
model_path = MODELS_DIR / "final_fake_job_detector.joblib"
artifact = joblib.load(model_path)

model = artifact["model"]
THRESHOLD = artifact["threshold"]

# Predictions generate karo
fake_scores = model.predict_proba(X_test)[:, 1]
predictions = (fake_scores >= THRESHOLD).astype(int)

# Results calculate karo
accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions, labels=[0, 1])

print("Final model artifact loaded successfully!")
print("Model:", artifact["model_name"])
print("Threshold:", THRESHOLD)
print("Test samples:", len(X_test))
print("Accuracy:", round(accuracy, 4))
print("Confusion matrix:")
print(cm)

# Expected results se compare karo
expected_cm = np.array([
    [3375, 28],
    [32, 141],
])

if np.array_equal(cm, expected_cm):
    print("\nVERIFICATION PASSED: Results match!")
else:
    print("\nVERIFICATION FAILED: Results do not match.")
    print("Check the model artifact, test split, and threshold.")
