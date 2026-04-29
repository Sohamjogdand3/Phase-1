#DataFrame = table (rows + columns)
# 2D-Table

import pandas as pd 

Data = {
    "Name": ["A", "B"],
    "Marks": [80, 90]
}

df = pd.DataFrame(Data)
print(df)
print(df["Marks"])
print(df[["Name", "Marks"]])
print(df.shape)