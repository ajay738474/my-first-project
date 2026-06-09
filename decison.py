import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
data={"age":[22,25,30,35,40],
      "purchased":[0,0,1,1,1]}
df=pd.DataFrame(data)
X=df[["age"]]
y=df["purchased"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model=DecisionTreeClassifier()
model.fit(X_train,y_train)
Y_pred=model.predict(X_test)
print("Predicted values:", Y_pred)