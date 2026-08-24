import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv("sales_dataset.csv")

X = df[["marketing_budget(thousands)"]]
y = df["actual_sales(millions)"]

model = LinearRegression()
model.fit(X, y)

r2 = model.score(X, y)
slope = model.coef_[0]
intercept = model.intercept_

plt.figure(figsize=(9, 6))
sns.regplot(
    x="marketing_budget(thousands)",
    y="actual_sales(millions)",
    data=df,
    color="tab:blue",
    marker="o",
    scatter_kws={"alpha": 0.6},
)
plt.title(
    "Linear Regression: Marketing Budget vs Actual Sales",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Marketing Budget (thousands of USD)", fontsize=11)
plt.ylabel("Actual Sales (millions of USD)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.5)

equation_text = (
    f"Sales = {slope:.4f} * Budget + {intercept:.4f}\nR² = {r2:.3f}"
)
plt.gca().text(
    0.05,
    0.85,
    equation_text,
    transform=plt.gca().transAxes,
    fontsize=11,
    verticalalignment="top",
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="white",
        alpha=0.8,
        edgecolor="gray",
    ),
)

plt.tight_layout()
plt.show()