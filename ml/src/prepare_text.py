import os
import joblib
from scipy.sparse import save_npz

from sklearn.feature_extraction.text import TfidfVectorizer
# 1. Required libraries import karo
import re
import html
import pandas as pd

# 2. Cleaned CSV file ka path
file_path = r"E:\fake-job-detector\ml\data\fake_job_postings_cleaned.csv"

# 3. CSV read karke DataFrame banao
df = pd.read_csv(file_path)

# 4. NLP ke liye use hone wale text columns
text_columns = [
    "title",
    "company_profile",
    "description",
    "requirements",
    "benefits"
]

# 5. Har job ke paanch text fields ko ek string mein jodo
df["combined_text"] = (
    df[text_columns]
    .fillna("")
    .agg(" ".join, axis=1)
)

print("Combined text created.")

# 6. Pehli job ka combined text dikhao
# print("\nFirst job:")
# print(df["combined_text"].iloc[0])

# 7. Pehli job ke text ke characters count karo
# print("\nOriginal text length:")
# print(len(df["combined_text"].iloc[0]))

# 8. Lowercase ka preview dikhao
# Note: isse original column change nahi hota
# print("\nLowercase preview:")
# print(df["combined_text"].iloc[0].lower()[:300])

# 9. Completely empty combined texts count karo
# print("\nTotal empty combined texts:")
# print(df["combined_text"].str.strip().eq("").sum())


# 10. Reusable preprocessing function define karo
def preprocess_text(text):
    # HTML entities decode karo
    text = html.unescape(str(text))

    # Text ko lowercase karo
    text = text.lower()

    # Multiple whitespace ko ek space mein badlo
    # Aur start/end ki extra spaces hatao
    text = re.sub(r"\s+", " ", text).strip()

    # Processed text return karo
    return text


# 11. Function ko har combined-text row par apply karo
# Result ek naye column mein store hota hai
df["cleaned_text"] = df["combined_text"].apply(preprocess_text)

# 12. Before aur after compare karo
# print("\nBefore preprocessing:")
# print(df["combined_text"].iloc[0][:300])

# print("\nAfter preprocessing:")
# print(df["cleaned_text"].iloc[0][:300])

# 13. Processed rows count karo
# print("\nTotal rows processed:")
# print(len(df["cleaned_text"]))


# Create TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=5000)

# Convert cleaned text into numerical features
tfidf_matrix = tfidf_vectorizer.fit_transform(df["cleaned_text"])

print("\nTF-IDF transformation completed.")
print("TF-IDF matrix shape:", tfidf_matrix.shape)
print("Vocabulary size:", len(tfidf_vectorizer.vocabulary_))


# Inspect TF-IDF features and values
feature_names = tfidf_vectorizer.get_feature_names_out()

# print("\nFirst 20 TF-IDF features:")
# print(feature_names[:20])

# print("\nFirst job's TF-IDF values:")
# print(tfidf_matrix[0].toarray()[0][:20])


# Inspect non-zero TF-IDF features in the first job
first_job_vector = tfidf_matrix[0]
nonzero_indices = first_job_vector.indices
nonzero_values = first_job_vector.data

# print("\nFirst job's non-zero TF-IDF features:")

# for index, value in zip(nonzero_indices[:15], nonzero_values[:15]):
#     print(f"{feature_names[index]}: {value:.4f}")


    
# Save processed text data
output_path = r"E:\fake-job-detector\ml\data\fake_job_postings_nlp.csv"

df.to_csv(output_path, index=False)

print("\nProcessed text data saved successfully!")
print("Saved file:", output_path)




# Save TF-IDF artifacts for reuse
models_dir = r"E:\fake-job-detector\ml\models"
os.makedirs(models_dir, exist_ok=True)

vectorizer_path = os.path.join(models_dir, "tfidf_vectorizer.joblib")
matrix_path = os.path.join(models_dir, "tfidf_matrix.npz")

joblib.dump(tfidf_vectorizer, vectorizer_path)
save_npz(matrix_path, tfidf_matrix)

print("\nTF-IDF artifacts saved successfully!")
print("Vectorizer:", vectorizer_path)
print("Matrix:", matrix_path)
