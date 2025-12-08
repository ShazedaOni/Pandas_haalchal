import pandas as pd
data = {
    "Name": ["Oni", "Tanji", "Opi", "Oyan", "Araf", "Ariba","Ayra","Shanta", "Ranu", "S.Alam"],
    "Age": [26, 24, 21, 20, 11, 7, 1,32, 45, 54],
    "Salary": [25000, 65000, 12000, 4000, 5000, 2000, 1000000, 40000, 630000, 50000],
    "Performance Score": [87, 86, 54, 67, 90, 98, 76, 78, 98, 92]


}

df = pd.DataFrame(data)
print(df)
#square brackets for new data adding df["Column_Name"] = some_Data

df["Bonus"] = df['Salary'] * 0.1
print(df)

# using insert() for specific position: df.insert(loc, "Column_Name", some_data)
df.insert(0, "Employee ID: ", [1,2,3,4,5,6,7,8,9,10])
print(df)