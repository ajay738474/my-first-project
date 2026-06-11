from sklearn.metrics import accuracy_score

y_test = [1, 0, 1, 1]
y_pred = [1, 0, 0, 1]

accuracy = accuracy_score(y_test, y_pred)

print(accuracy)