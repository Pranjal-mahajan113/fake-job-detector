
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
print("\nFirst job:")
print(df["combined_text"].iloc[0])

# 7. Pehli job ke text ke characters count karo
print("\nOriginal text length:")
print(len(df["combined_text"].iloc[0]))

# 8. Lowercase ka preview dikhao
# Note: isse original column change nahi hota
print("\nLowercase preview:")
print(df["combined_text"].iloc[0].lower()[:300])

# 9. Completely empty combined texts count karo
print("\nTotal empty combined texts:")
print(df["combined_text"].str.strip().eq("").sum())


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
print("\nBefore preprocessing:")
print(df["combined_text"].iloc[0][:300])

print("\nAfter preprocessing:")
print(df["cleaned_text"].iloc[0][:300])

# 13. Processed rows count karo
print("\nTotal rows processed:")
print(len(df["cleaned_text"]))