from sklearn.tree import DecisionTreeClassifier

X = [[20], [25], [30], [35]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[28]])

print(prediction)