# Lab Assignment 2

# Input prices of sold items
prices = tuple(map(float, input("Enter prices of sold items separated by space: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Cheapest item price
print("Cheapest item price:", min(prices))

# c) Costliest item price
print("Costliest item price:", max(prices))

# d) Prices in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
costliest_count = prices.count(max(prices))
print("Number of costliest items sold:", costliest_count)
