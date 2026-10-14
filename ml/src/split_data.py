import pandas as pd
from scipy.sparse import load_npz
from sklearn.model_selection import train_test_split

# Load the cleaned dataset containing labels
data_path = r"E:\fake-job-detector\ml\data\fake_job_postings_cleaned.csv"
df = pd.read_csv(data_path)

# Load the saved TF-IDF matrix
matrix_path = r"E:\fake-job-detector\ml\models\tfidf_matrix.npz"
X = load_npz(matrix_path)

# Target labels: 0 = real, 1 = fake
y = df["fraudulent"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Data split completed!")
print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)
print("\nTraining labels:")
print(y_train.value_counts())
print("\nTesting labels:")
print(y_test.value_counts())
