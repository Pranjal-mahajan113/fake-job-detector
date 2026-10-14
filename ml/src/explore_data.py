import pandas as pd

file_path = r"E:\fake-job-detector\ml\data\fake_job_postings.csv"

df = pd.read_csv(file_path)

# print("Dataset shape:")
# print(df.shape)

# print("\nColumn names:")
# print(df.columns.tolist())

# print("\nDataset information:")
# print(df.info())

# print("\nFraudulent value counts:")
# print(df["fraudulent"].value_counts())

# print("\nFraudulent percentage:")
# print(df["fraudulent"].value_counts(normalize=True) * 100)

# Graph
# import matplotlib.pyplot as plt

# fraud_counts = df["fraudulent"].value_counts()

# plt.bar(["Real", "Fake"], fraud_counts.values)

# plt.title("Real vs Fake Job Postings")
# plt.xlabel("Job Type")
# plt.ylabel("Number of Job Postings")

# plt.show()
# print("\nMissing values:")
# print(df.isnull().sum())

# print("\nEmployment type distribution:")
# print(df["employment_type"].value_counts(dropna=False))

# print("\nEmployment type vs fraudulent:")
# print(
#     pd.crosstab(
#         df["employment_type"],
#         df["fraudulent"],
#         margins=True
#     )
#)
# print("\nRequired experience distribution:")
# print(df["required_experience"].value_counts(dropna=False))
# print("\nRequired education distribution:")
# print(df["required_education"].value_counts(dropna=False))

# print("\nIndustry distribution:")
# print(df["industry"].value_counts(dropna=False).head(20))

# print("\nFunction distribution:")
# print(df["function"].value_counts(dropna=False).head(20))

# print("\nDuplicate rows:")
# print(df.duplicated().sum())

# print("\nEmpty strings:")
# for column in df.columns:
#     empty_count = (df[column] == "").sum()
#     if empty_count > 0:
#         print(column, empty_count)

# print("\nText columns:")
# print(df.select_dtypes(include="str").columns.tolist())

# print("\nWhitespace-only values:")

# for column in df.select_dtypes(include="str").columns:
#     whitespace_count = df[column].fillna("").str.strip().eq("").sum()

#     if whitespace_count > 0:
#         print(column, whitespace_count)


# print("\nMissing values after treating whitespace as missing:")

# for column in df.columns:
#     missing_count = (
#         df[column]
#         .astype("string")
#         .str.strip()
#         .eq("")
#         .sum()
#     )

#     nan_count = df[column].isna().sum()

#     total_missing = max(missing_count, nan_count)

#     if total_missing > 0:
#         print(column, total_missing)

