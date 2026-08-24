import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("sales_dataset.csv")

X = df[["marketing_budget(thousands)"]]
y = df["actual_sales(millions)"]

model = LinearRegression()
model.fit(X, y)

r_squared = model.score(X, y)
print("R-squared Value:", r_squared)