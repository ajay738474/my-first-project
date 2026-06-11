import pandas as pd

data = {
    "Age": [20, None, 30]
}

df = pd.DataFrame(data)

df["Age"].fillna(df["Age"].mean(), inplace=True)

print(df)