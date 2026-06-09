import panda as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_encoder
from sklearn .preprocessing import standard_scaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
data={"Gender":["male","female","male","female"],
      "Age":[20,None,25,30,35],
      "purchased":["yes","no","yes","no","yes",]}
df=pd.DataFrame(data)
print(df.isnull().sum())
df['Age'].fillna(df['Age'].mean(),inplace=True)
df["Gender"].fillna(df["Gender"],inplace=True)
le=label_encoder()
df["gender_encoded"]=le.fit_transform(df["Gender"])
df["purchased_encoded"]=le.fit_transform(df["purchased"])
X=["gender"],["Age"]
Y=["purchased_encoded"]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
scaler=standard_scaler()
X_train_scaled=scaler.fit_transform(X_train)
model=LogisticRegression()
model.fit(X_train_scaled,Y_train)
model.predict(X_test)
accuracy=accuracy_score(Y_test,model.predict(X_test))
cm=confusion_matrix(Y_test,y_pred=)
print(cm)
print("Accuracy:",accuracy)
print(X_train)
print(X_test)





