import pandas as pd

df = pd.DataFrame({
    "Bedrooms": [2, 3, 4],
    "Bathrooms": [1, 2, 3]
})

df["Total_Rooms"] = df["Bedrooms"] + df["Bathrooms"]

print(df)