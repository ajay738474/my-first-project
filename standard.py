from sklearn.preprocessing import StandardScaler

X = [[20], [25], [30], [35]]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print(X_scaled)