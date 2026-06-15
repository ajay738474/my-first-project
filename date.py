import pandas as pd

df = pd.DataFrame({
    "Date": ["2025-01-15", "2025-06-10", "2025-12-25"]
})

df["Month"] = pd.to_datetime(df["Date"]).dt.month

print(df)