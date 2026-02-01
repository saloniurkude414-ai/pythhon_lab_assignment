# Input voltage and resistance
V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (Ohms): "))

# Calculate current
I = V / R

# Display result
print("Current (I) =", I, "A")

# Input voltage and resistance
V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (Ohms): "))

# Calculate current using Ohm's Law
I = V / R

print("Current (I) =", I, "A")

# Determine nature of current
if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")
