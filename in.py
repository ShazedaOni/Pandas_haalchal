import pandas as pd

df = pd.read_json("sample_Data.json")
print("disoyaing the info of data set")

print(df.info())

data = {
    "Name": ['Oni', 'Tanji', 'Rubina'],
    "Age" : [26,24,27],
    "city": ["Feni", "chandpur", "Lokkhipur"]
}

df = pd.DataFrame(data)
print(df.info())
