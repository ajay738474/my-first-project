import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
X=[[1,2],[2,3],[3,3],[6,5],[7,8],[8,8]]
Y=[0,0,0,1,1,1]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.33,random_state=42)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test) 
model=SVC(kernel='linear')
model.fit(X_train,Y_train)  
y_pred=model.predict(X_test)
accuracy=accuracy_score(Y_test,y_pred)
print("Accuracy:",accuracy)