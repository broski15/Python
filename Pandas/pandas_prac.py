import pandas as pd

mydatasets = {
    "name":["rohan", "praveen", "dilip", "rupesh"],
    "age":[28,31,33,30],
    "salary":[50000,30000,40000,60000]
}

df = pd.DataFrame(mydatasets)

print(df)