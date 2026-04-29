import pandas as pd

s = pd.Series([10, 20, 30])
print(s)
print(s[0]) # by using index


a = pd.Series([1,2,3], index=["a","b","c"])
print(a) 
print(a["a"]) 
print(a[0:2])

print(a.shape)
print(a.dtype)