import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
df = pd.read_csv('data.csv')
print(df.isnull().sum())
le=LabelEncoder()
df["sex"]=le.fit_transform(df["sex"])
X=df[["Pclass","sex","age","fare"]]
Y=df["survived"]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(Y_test, y_pred))
print("Classification Report:")
print(classification_report(Y_test, y_pred))
