from sklearn.linear_model import LogisticRegression

X = [[20], [25], [30], [35]]
y = [0, 0, 1, 1]

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[28]])

print(prediction)