import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("sales_dataset.csv")

X = df[["marketing_budget(thousands)"]]
y = df["actual_sales(millions)"]

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)