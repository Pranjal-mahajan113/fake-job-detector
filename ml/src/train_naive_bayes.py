
import joblib
from pathlib import Path

import pandas as pd
from scipy.sparse import load_npz
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load target labels
data_path = r"E:\fake-job-detector\ml\data\fake_job_postings_cleaned.csv"

df = pd.read_csv(data_path)
y = df["fraudulent"]

# Load TF-IDF features
matrix_path = r"E:\fake-job-detector\ml\models\tfidf_matrix.npz"

X = load_npz(matrix_path)

print("Features loaded:", X.shape)
print("Labels loaded:", y.shape)


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


# Create the Naive Bayes model
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

print("\nNaive Bayes training completed!")

# Predict test labels
y_pred = model.predict(X_test)


# Calculate evaluation results
accuracy = accuracy_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

report = classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Real (0)", "Fake (1)"],
    zero_division=0
)

# Display results
print("\nAccuracy:", accuracy)

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(report)


# Create results folder if needed
results_dir = Path(r"E:\fake-job-detector\ml\results")
results_dir.mkdir(parents=True, exist_ok=True)

# Save evaluation results
results_path = results_dir / "naive_bayes.txt"

with open(results_path, "w", encoding="utf-8") as file:
    file.write("Multinomial Naive Bayes - Results\n")
    file.write("=" * 40 + "\n")
    file.write(f"Training samples: {X_train.shape[0]}\n")
    file.write(f"Testing samples: {X_test.shape[0]}\n")
    file.write(f"Accuracy: {accuracy:.4f}\n\n")
    file.write("Confusion Matrix:\n")
    file.write(str(cm) + "\n\n")
    file.write("Classification Report:\n")
    file.write(report)

print("\nResults saved at:", results_path)


# Save trained model
model_path = r"E:\fake-job-detector\ml\models\naive_bayes_model.joblib"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Saved at:", model_path)
