import pandas as pd

data = {
    "Name": ['Oni', 'Tanji', 'Rubina'],
    "Age" : [26,24,27],
    "city": ["Feni", "chandpur", "Lokkhipur"]
}

df = pd.DataFrame(data)
print(df)

# df.to_csv("Output.csv", index = False)
# df.to_excel("Output.xlsx", index = False)
df.to_json("Output.json", index = False)
 
 
 
# df = pd.read_csv("Output.csv")
# print(df)