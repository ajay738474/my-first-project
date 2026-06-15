import pandas as pd

df = pd.DataFrame({
    "Weight": [70, 80, 60],
    "Height": [1.70, 1.80, 1.65]
})

df["BMI"] = df["Weight"] / (df["Height"] ** 2)

print(df)