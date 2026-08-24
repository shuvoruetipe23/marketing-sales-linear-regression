import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("sales_dataset.csv")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(
    df["marketing_budget(thousands)"], kde=True, color="tab:blue", bins=20
)
plt.title("Distribution of Marketing Budget", fontsize=12, fontweight="bold")
plt.xlabel("Marketing Budget (thousands)", fontsize=10)
plt.ylabel("Density / Count", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)

plt.subplot(1, 2, 2)
sns.histplot(df["actual_sales(millions)"], kde=True, color="tab:green", bins=20)
plt.title("Distribution of Actual Sales", fontsize=12, fontweight="bold")
plt.xlabel("Actual Sales (millions)", fontsize=10)
plt.ylabel("Density / Count", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()