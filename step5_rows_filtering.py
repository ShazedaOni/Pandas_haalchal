import pandas as pd
data = {
    "Name": ["Oni", "Tanji", "Opi", "Oyan", "Araf", "Ariba","Ayra","Shanta", "Ranu", "S.Alam"],
    "Age": [26, 24, 21, 20, 11, 7, 1,32, 45, 54],
    "Salary": [25000, 65000, 12000, 4000, 5000, 2000, 1000000, 40000, 630000, 50000],
    "Performance Score": [87, 86, 54, 67, 90, 98, 76, 78, 98, 92]

}

df = pd.DataFrame(data)
print("Sample dataFrame")
print(df) 

high_salary = df[df["Salary"] > 50000]
print('Employees with salary > 50000')
print(high_salary)

high_salary = df[df["Salary"] >= 50000]
print('Employees with salary > 50000')
print(high_salary)

# filtering rows salary > 50k & age 30
filtered = df[(df['Age'] > 30) & (df['Salary'] >= 50000)]
print(f'Employee list Age > 30 + Salary > 50000')
print(filtered)
filtered_or = df[(df['Age'] > 35) | (df['Performance Score'] >= 90)]
print(f'Employee list Age > 35 + Performance Score > 90')
print(filtered_or)