from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4]]
y = [10, 20, 30, 40]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[5]])

print(prediction)