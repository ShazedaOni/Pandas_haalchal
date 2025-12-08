import pandas as pd
data = {
    "Name": ["Oni", "Tanji", "Opi", "Oyan", "Araf", "Ariba","Ayra","Shanta", "Ranu", "S.Alam"],
    "Age": [26, 24, 21, 20, 11, 7, 1,32, 45, 54],
    "Salary": [25000, 65000, 12000, 4000, 5000, 2000, 1000000, 40000, 630000, 50000],
    "Performance Score": [87, 86, 54, 67, 90, 98, 76, 78, 98, 92]


}

df = pd.DataFrame(data) 
print(df) 

# .loc[], specific value er jnno
# df.loc[row_index, "Column Name"] = new_value
df.loc[0, 'Salary'] = 55000
print(df)