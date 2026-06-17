import pandas as pd
from sklearn.cluster import KMeans

df = pd.DataFrame({
    "Spending": [500, 600, 700, 5000, 5500, 6000]
})

X = df[["Spending"]]

model = KMeans(n_clusters=2, random_state=42)

model.fit(X)


df["Cluster"] = model.labels_

print(df)
print("Centroids:")
print(model.cluster_centers_)