import pandas as pd

# Read CSV file
df = pd.read_csv("Book.csv")

# Display column names (optional for debugging)
# print(df.columns)

# a) Complete report
print("\nComplete Book Report:")
print(df.to_string(index=False))

# b) Books by given author
author = input("\nEnter author name: ").strip()
result_author = df[df['author'].str.lower() == author.lower()]

print("\nBooks by author:")
if not result_author.empty:
    print(result_author.to_string(index=False))
else:
    print("No books found for this author.")

# c) Books by publishing house
pub = input("\nEnter publishing house: ").strip()
result_pub = df[df['publishing_house'].str.lower() == pub.lower()]

print("\nBooks by publishing house:")
if not result_pub.empty:
    print(result_pub.to_string(index=False))
else:
    print("No books found for this publishing house.")

# d) Cheapest and costliest book
cheapest = df[df['price'] == df['price'].min()]
costliest = df[df['price'] == df['price'].max()]

print("\nCheapest Book:")
print(cheapest[['title', 'price']].to_string(index=False))

print("\nCostliest Book:")
print(costliest[['title', 'price']].to_string(index=False))

# e) Sort by year
print("\nBooks sorted by year:")
print(df.sort_values(by='year').to_string(index=False))