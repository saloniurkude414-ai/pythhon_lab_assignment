import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (you can replace with CSV file)
data = {
    "month": list(range(1,13)),
    "facecream": [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    "facewash": [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760],
    "toothpaste": [5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400],
    "bathingsoap": [9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400],
    "shampoo": [1200,2100,3550,1870,1560,1890,1780,2100,2300,2400,1800,2100],
    "moisturizer": [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760],
    "total_profit": [211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]
}

df = pd.DataFrame(data)

# a) Line Plot - Total Profit
plt.plot(df['month'], df['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline Plot - All products
plt.plot(df['month'], df['facecream'], label="Face Cream")
plt.plot(df['month'], df['facewash'], label="Face Wash")
plt.plot(df['month'], df['toothpaste'], label="Toothpaste")
plt.legend()
plt.title("Sales Data")
plt.show()

# c) Bar Chart - Face Cream & Face Wash
x = df['month']
plt.bar(x-0.2, df['facecream'], width=0.4, label="Face Cream")
plt.bar(x+0.2, df['facewash'], width=0.4, label="Face Wash")
plt.legend()
plt.title("Bar Chart")
plt.show()

# d) Pie Chart - Total yearly sales
total_sales = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

labels = ["Face Cream","Face Wash","Toothpaste","Soap","Shampoo","Moisturizer"]

plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Yearly Sales Distribution")
plt.show()