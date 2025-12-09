import pandas as pd
data = {
    "Name": ["Oni",None, "Tanji", "Opi", "Oyan", "Araf", "Ariba", "Ayra","Shanta", "Ranu", "S.Alam"],
    "Age": [26,None, 24, 21, 20, 11, 7, 1,32, 45, 54],
    "Salary": [25000,None, 65000, 12000, 4000, 5000, 2000, 1000000, 40000, 630000, 50000],
    "Performance Score": [87,None, 86, 54, 67, 90, 98, 76, 78, 98, 92]


}

df = pd.DataFrame(data)
print(df) 

# dropna() - ei method diye kono missing value ba null valu vanish kore dite parbe

# df.dropna(axis =1, inplace = True) axis- 0 mane rows er missing value baad deya, axis-1 mane column er missig value baad deya

df.dropna(inplace=True)
print(df)