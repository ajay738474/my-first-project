from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print(X_train)
print(X_test)