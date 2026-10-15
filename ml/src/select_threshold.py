
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# Project paths
ML_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ML_DIR / "data"
RESULTS_DIR = ML_DIR / "results"

# Dataset load karo
df = pd.read_csv(DATA_DIR / "fake_job_postings_nlp.csv")

X = df["cleaned_text"].fillna("").astype(str)
y = df["fraudulent"].astype(int)

# Pehle wahi original train/test split banao
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Original training data ka ek hissa validation ke liye alag karo
X_subtrain, X_val, y_subtrain, y_val = train_test_split(
    X_train,
    y_train,
    test_size=0.2,
    random_state=42,
    stratify=y_train
)

print("Training samples:", len(X_subtrain))
print("Validation samples:", len(X_val))
print("Final test samples (abhi untouched):", len(X_test))

# Model sirf sub-training data par seekhega
model = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

model.fit(X_subtrain, y_subtrain)

# Validation jobs ke fake hone ke scores
fake_scores = model.predict_proba(X_val)[:, 1]

# Alag-alag thresholds compare karo
results = []

for threshold in [0.50, 0.60, 0.70, 0.80]:
    predictions = (fake_scores >= threshold).astype(int)

    tn, fp, fn, tp = confusion_matrix(
        y_val, predictions, labels=[0, 1]
    ).ravel()

    precision = precision_score(
        y_val, predictions, zero_division=0
    )
    recall = recall_score(
        y_val, predictions, zero_division=0
    )
    f1 = f1_score(
        y_val, predictions, zero_division=0
    )

    results.append({
        "threshold": threshold,
        "false_positives": fp,
        "false_negatives": fn,
        "true_positives": tp,
        "true_negatives": tn,
        "fake_precision": round(precision, 4),
        "fake_recall": round(recall, 4),
        "fake_f1": round(f1, 4),
    })

results_df = pd.DataFrame(results)

RESULTS_DIR.mkdir(parents=True, exist_ok=True)
output_path = RESULTS_DIR / "validation_threshold_comparison.csv"
results_df.to_csv(output_path, index=False)

print("\nValidation threshold comparison:")
print(results_df.to_string(index=False))
print("\nSaved results:", output_path)
