
import joblib
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Project ke folders ke paths
ML_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ML_DIR / "data"
MODELS_DIR = ML_DIR / "models"

# Cleaned text aur labels load karo
data_path = DATA_DIR / "fake_job_postings_nlp.csv"
df = pd.read_csv(data_path)

X = df["cleaned_text"].fillna("").astype(str)
y = df["fraudulent"].astype(int)

# Raw text ko pehle training aur testing mein split karo
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Split ko save karo, taaki sabhi models same data use karein
MODELS_DIR.mkdir(parents=True, exist_ok=True)

split_path = MODELS_DIR / "train_test_text_split.joblib"

joblib.dump(
    {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
    },
    split_path
)

print("Text split completed successfully!")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("\nTraining labels:")
print(y_train.value_counts())
print("\nTesting labels:")
print(y_test.value_counts())
print("\nSaved split:", split_path)
