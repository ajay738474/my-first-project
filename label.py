from sklearn.preprocessing import LabelEncoder

data = ["Male", "Female", "Male"]

le = LabelEncoder()

encoded = le.fit_transform(data)

print(encoded)