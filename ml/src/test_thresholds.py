
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# Load the dataset
df = pd.read_csv("ml/data/fake_job_postings_nlp.csv")

X = df["cleaned_text"].fillna("").astype(str)
y = df["fraudulent"].astype(int)

# Recreate the same train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Load the trained model
model = joblib.load(
    "ml/models/logistic_regression_balanced_pipeline.joblib"
)

# Get the model's score for the Fake class (label 1)
fake_scores = model.predict_proba(X_test)[:, 1]

# Try different thresholds
for threshold in [0.50, 0.60, 0.70, 0.80]:
    predictions = (fake_scores >= threshold).astype(int)

    tn, fp, fn, tp = confusion_matrix(
        y_test, predictions, labels=[0, 1]
    ).ravel()

    precision = precision_score(
        y_test, predictions, zero_division=0
    )
    recall = recall_score(
        y_test, predictions, zero_division=0
    )
    f1 = f1_score(
        y_test, predictions, zero_division=0
    )

    print(f"\nThreshold: {threshold:.2f}")
    print(f"Real jobs wrongly flagged as Fake (FP): {fp}")
    print(f"Fake jobs correctly detected (TP): {tp}")
    print(f"Fake jobs missed (FN): {fn}")
    print(f"Fake precision: {precision:.3f}")
    print(f"Fake recall: {recall:.3f}")
    print(f"Fake F1-score: {f1:.3f}")
