import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_dataset.csv")

print(df.describe())

correlation = df.corr()
print("\nCorrelation Matrix:\n", correlation)

plt.figure(figsize=(8, 6))
sns.regplot(
    x="marketing_budget(thousands)",
    y="actual_sales(millions)",
    data=df,
    color="blue",
    marker="o",
)
plt.title("Marketing Budget vs Actual Sales")
plt.xlabel("Marketing Budget (thousands)")
plt.ylabel("Actual Sales (millions)")
plt.grid(True)
plt.show()