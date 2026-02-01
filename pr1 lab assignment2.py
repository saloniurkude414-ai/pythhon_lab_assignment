# Vendor details
name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

# Monthly purchases
monthly_purchase = []
print("\nEnter monthly purchase amounts:")
for i in range(12):
    amount = float(input(f"Month {i+1}: "))
    monthly_purchase.append(amount)

# Annual purchase calculation
annual_total = sum(monthly_purchase)

# Display Annual Billing Report
print("\n----- Annual Purchase / Billing Report -----")
print("Vendor Name        :", name)
print("Year of Association:", year)
print("Contact Number     :", contact)
print("Email ID           :", email)
print("Annual Purchase    : Rs.", annual_total)
