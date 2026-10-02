import pandas as pd

input_file = r"E:\fake-job-detector\ml\data\fake_job_postings.csv"
output_file = r"E:\fake-job-detector\ml\data\fake_job_postings_cleaned.csv"

df = pd.read_csv(input_file)

# NLP text columns
text_columns = [
    "title",
    "company_profile",
    "description",
    "requirements",
    "benefits"
]

# Categorical columns
categorical_columns = [
    "location",
    "department",
    "employment_type",
    "required_experience",
    "required_education",
    "industry",
    "function"
]

# Salary column
salary_column = "salary_range"

# Clean whitespace in text/categorical columns
for column in text_columns + categorical_columns + [salary_column]:
    df[column] = df[column].astype("string").str.strip()

# Fill missing NLP text with empty string
for column in text_columns:
    df[column] = df[column].fillna("")

# Fill missing categorical values
for column in categorical_columns:
    df[column] = df[column].fillna("Not Specified")

# Fill missing salary information
df[salary_column] = df[salary_column].fillna("Not Specified")

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("Cleaned dataset saved successfully.")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nRemaining missing values:")
print(df.isna().sum())


print("\nDataset shape:")
print(df.shape)

print("\nFraudulent values:")
print(df["fraudulent"].value_counts())

print("\nUnique fraudulent values:")
print(df["fraudulent"].unique())
