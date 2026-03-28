import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Complete report
print("Complete Book Report:")
print(df)

# b) Books by a given author
author = "John Smith"
print("\nBooks by Author:", author)
print(df[df["Author"] == author])

# c) Books by a given publisher
publisher = "XYZ Pub"
print("\nBooks by Publisher:", publisher)
print(df[df["Publisher"] == publisher])

# d) Cheapest and costliest books
print("\nCheapest Book:")
print(df.loc[df["Price"].idxmin()]["Title"])

print("\nCostliest Book:")
print(df.loc[df["Price"].idxmax()]["Title"])

# e) Sorted by year
print("\nBooks Sorted by Year:")
print(df.sort_values(by="Year"))