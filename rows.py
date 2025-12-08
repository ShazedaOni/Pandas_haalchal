#head() tail()
#head() 5
#tail() 5

import pandas as pd


df = pd.read_json("sample_Data.json")
print("display 10 rows of first")
print(df.head(10))

print("display 10 rows of last")
print(df.tail(10))
print("display rows of first")
print(df.head())

print("display  rows of last")
print(df.tail())
#head() tail( e value dile first and last er tototai row dekhabe, but value na dile first er 5ta and last er 5 ta rows dekhabe)