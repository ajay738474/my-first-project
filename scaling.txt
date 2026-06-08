import pandas as pd
from sklearn.preprocessing import StandardScaler
data={"Age":[20,25,30,35],
      "salary":[30000,50000,70000,90000]}
df=pd.DataFrame(data)
X=df[["Age","salary"]]
scaler=StandardScaler()
scaler.fit_transform(X)
print(scaler.fit_transform(X))









