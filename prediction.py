import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("sales_dataset.csv")

X = df[["marketing_budget(thousands)"]]
y = df["actual_sales(millions)"]

model = LinearRegression()
model.fit(X, y)

new_budget = pd.DataFrame({"marketing_budget(thousands)": [300, 350, 400]})
predicted_sales = model.predict(new_budget)

for budget, sales in zip(new_budget["marketing_budget(thousands)"], predicted_sales):
    print(f"Budget: {budget} -> Predicted Sales: {sales:.2f}")