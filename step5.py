"""
problems which arise:
1- select specific column
2- filter rows
3- combine multiple condition

solution which given pandas:
1- square brackts
2- boolean conditions

selectiong columns:
1- a series return korbe , or
2- dataframe return korbe(jodi multiple data hoy)

example:
column = df["column Name]
subset = df["column1", "column2"....]

filtering rows:
1- boolean indexing return(condition wise data extract korte hbe)

based on a single condition:
filtered_rows = df{df["Salary"]>50000}

combine multiple conditions:
filtered_rows = df{(df[Salary"]> 50000) & (df["column2])< 80000}
"""

import pandas as pd
data = {
    "Name": ["Oni", "Tanji", "Opi", "Oyan", "Araf", "Ariba","Ayra","Shanta", "Ranu", "S.Alam"],
    "Age": [26, 24, 21, 20, 11, 7, 1,32, 45, 54],
    "Salary": [25000, 45000, 12000, 4000, 5000, 2000, 1000, 40000, 30000, 50000],
    "Performance Score": [87, 86, 54, 67, 90, 98, 76, 78, 98, 92]

}

df = pd.DataFrame(data)
print("Sample dataFrame")
print(df)

print("Names (Single column return series)")
name = df["Name"]
print(name)

#selecting multiple columns:

subset = df[["Name", "Salary"]]
print("\nSubset with Name and Salary")
print(subset)


