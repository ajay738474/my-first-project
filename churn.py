import pandas as pd
data = {
    "Age": [25, 35, 40, 28, 50],
    "Salary": [30000, 60000, 70000, 40000, 90000],
    "Balance": [5000, 15000, 20000, 8000, 25000],
    "Churn": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
df=pd.DataFrame()
df.head(5)
X=[["age","salary","balance"]]
Y=[["churn"]]
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
from sklearn.linear_model import LogisticRegression 
model=LogisticRegression()
model.fit(X_train,Y_train)
predictions=model.predict(X_test)
print(predictions)  
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(Y_test, predictions)
print("Accuracy:", accuracy)