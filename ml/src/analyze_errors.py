
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the same dataset used in our corrected workflow
df = pd.read_csv("ml/data/fake_job_postings_nlp.csv")

X = df["cleaned_text"].fillna("").astype(str)
y = df["fraudulent"].astype(int)

# Recreate the same held-out test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Load our trained pipeline
model = joblib.load(
    "ml/models/logistic_regression_balanced_pipeline.joblib"
)

predictions = model.predict(X_test)

# Find real jobs incorrectly predicted as fake
false_positive_positions = [
    i for i, (actual, predicted) in enumerate(
        zip(y_test.to_numpy(), predictions)
    )
    if actual == 0 and predicted == 1
]

print("False positives found:", len(false_positive_positions))

# Show five examples for investigation
for i in false_positive_positions[:5]:
    row_index = X_test.index[i]
    row = df.loc[row_index]

    print("\n" + "=" * 60)
    print("Title:", row["title"])
    print("Actual label: Real")
    print("Predicted label: Fake")
    print("Description:")
    print(str(row.get("description", ""))[:700])
