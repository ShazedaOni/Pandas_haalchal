import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# df = pd.read_excel("SampleSuperstore.xlsx", engine="openpyxl")
df = pd.read_json("sample_Data.json")
print(df)
print(df)

# data cloud e store thakle ta read korar jnno #gcsfs ei library er maddhome oi google platform theke data read kora jabe
