import pandas as pd
data = {
    "Time": [1, 2, None, 4, 5],
    "Value": [10, None, 30, None, 50]
}
df = pd.DataFrame(data)
print("Before interpulation")
print(df)

df["Value"] = df["Value"].interpolate(method = "linear")
df["Time"] = df["Time"].interpolate(method = "linear")
print("After interpulation")
print(df)

"""When will use interpulation techniqyes:
1- timer series data
2- numeric data with trends
3- avoid dropping rows

disadv:
1- can't work with categorical data(name,id...)
2- predctable data might not be always exist
"""