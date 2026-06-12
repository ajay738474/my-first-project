import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("house_prices.csv")


X = df[[
    "SQFT",
    "Bedrooms",
    "Bathrooms",
    "Age",
    "LotSize",
    "WalkScore",
    "Income"
]]

y = df["Price"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

print("\nIntercept (β0):", model.intercept_)

print("\nCoefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")

new_house = pd.DataFrame({
    "SQFT": [1800],
    "Bedrooms": [3],
    "Bathrooms": [2],
    "Age": [8],
    "LotSize": [5500],
    "WalkScore": [82],
    "Income": [75000]
})

predicted_price = model.predict(new_house)

print("\nPredicted House Price: $", predicted_price[0])