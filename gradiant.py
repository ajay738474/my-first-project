from sklearn.ensemble import gradientboostingclassifier
model = gradientboostingclassifier(max_depth=3, n_estimators=100, learning_rate=0.1)
model.fit(X_train, y_train)
ypred = model.predict(X_test)
print("Predictions:", ypred)