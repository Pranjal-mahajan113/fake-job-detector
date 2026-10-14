import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import pandas as pd
from scipy.sparse import load_npz
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load target labels
data_path = r"E:\fake-job-detector\ml\data\fake_job_postings_cleaned.csv"
df = pd.read_csv(data_path)
y = df["fraudulent"]

# Load TF-IDF features
matrix_path = r"E:\fake-job-detector\ml\models\tfidf_matrix.npz"
X = load_npz(matrix_path)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create the Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

print("Logistic Regression training completed!")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Real (0)", "Fake (1)"],
    zero_division=0
))


model_path = r"E:\fake-job-detector\ml\models\logistic_regression_model.joblib"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Saved at:", model_path)