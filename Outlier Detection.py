import pandas as pd

df = pd.read_csv("sales_dataset.csv")

Q1 = df["actual_sales(millions)"].quantile(0.25)
Q3 = df["actual_sales(millions)"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["actual_sales(millions)"] < lower_bound)
    | (df["actual_sales(millions)"] > upper_bound)
]

print("Number of outliers:", len(outliers))
print("\nOutlier rows:\n", outliers)