import pandas as pd
data = {
    "Name": ["Oni",None, "Tanji", "Opi", "Oyan", "Araf", "Ariba", "Ayra","Shanta", "Ranu", "S.Alam"],
    "Age": [26,None, 24, 21, 20, 11, 7, 1,32, 45, 54],
    "Salary": [25000,None, 65000, 12000, 4000, 5000, 2000, 1000000, 40000, 630000, 50000],
    "Performance Score": [87,None, 86, 54, 67, 90, 98, 76, 78, 98, 92]


}

df = pd.DataFrame(data)
print(df) 

# fillna() - ei method diye kono missing value ba null valu vanish na kore replace kore dey. jeno data loss na hoy.

# df.fillna(value, inplace = True) 
df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)
df.fillna({
    "Age": df["Age"].mean(),
    "Salary": df["Salary"].median(),
    "Performance Score": df["Performance Score"].mean()
}, inplace=True)
print(df)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Performance Score'] = df['Performance Score'].fillna(df['Performance Score'].mean())

print(df)