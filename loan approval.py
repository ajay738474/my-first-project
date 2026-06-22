import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression  
from sklearn.metrics import accuracy_score  
df=pd.read_csv("file.csv")
df.head(5)
df.isnull().sum()
X=df[["gender","age","income"]]
Y=df[["Loan_Status"]]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)
model=LogisticRegression()
model.fit(X_train,Y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(Y_test,y_pred)
print("Accuracy:",accuracy)