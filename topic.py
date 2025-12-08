"""1 - how big is your dataset
    2- what are the names of columns

    use shape and columns
"""

import pandas as pd

data = {
    "Name": ["Oni", "Tanji", "Opi", "Oyan", "Araf", "Ariba","Ayra","Shanta", "Ranu", "S.Alam"],
    "Age": [26, 24, 21, 20, 11, 7, 1,32, 45, 54],
    "Salary": [25000, 45000, 12000, 4000, 5000, 2000, 1000, 40000, 30000, 50000],
    "Performance Score": [87, 86, 54, 67, 90, 98, 76, 78, 98, 92]

}

df = pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'Column Name: {df.columns}')