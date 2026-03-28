import pandas as pd

# Create DataFrame
data = {
    "State": ["State1", "State2", "State3", "State4", "State5"],
    "Area": [50000, 70000, 60000, 80000, 55000],
    "Population": [1000000, 1500000, 1200000, 2000000, 1100000]
}

df = pd.DataFrame(data)

# a) Complete info
print("Complete State Information:")
print(df)

# b) Largest Area
print("\nState with Largest Area:")
print(df.loc[df["Area"].idxmax()]["State"])

# c) Largest Population
print("\nState with Largest Population:")
print(df.loc[df["Population"].idxmax()]["State"])

# d) Population Density
df["Density"] = df["Population"] / df["Area"]
print("\nState with Density:")
print(df)

# e) Highest Density
print("\nState with Highest Population Density:")
print(df.loc[df["Density"].idxmax()]["State"])