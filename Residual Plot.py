import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv("sales_dataset.csv")

X = df[["marketing_budget(thousands)"]]
y = df["actual_sales(millions)"]

model = LinearRegression()
model.fit(X, y)

plt.figure(figsize=(9, 6))
sns.residplot(
    x=X.iloc[:, 0],
    y=y,
    lowess=True,
    color="tab:red",
    scatter_kws={"alpha": 0.6},
)
plt.title(
    "Residual Plot: Marketing Budget vs Residuals",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Marketing Budget (thousands of USD)", fontsize=11)
plt.ylabel("Residuals (Actual - Predicted)", fontsize=11)
plt.axhline(0, color="black", linestyle="--", linewidth=1)
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()