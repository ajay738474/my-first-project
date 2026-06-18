from xboost import XBoostclassifier
model = XBoostclassifier(n_estimators=100, learning_rate=0.1, max_depth=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)   
