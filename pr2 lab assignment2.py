# Input values
hardness = float(input("Enter hardness of steel: "))
carbon = float(input("Enter carbon content: "))
tensile = float(input("Enter tensile strength: "))

# Check conditions
c1 = hardness > 50
c2 = carbon < 0.7
c3 = tensile > 5600

# Determine grade
if c1 and c2 and c3:
    grade = 10
elif c1 and c2:
    grade = 9
elif c2 and c3:
    grade = 8
elif c1 and c3:
    grade = 7
elif c1 or c2 or c3:
    grade = 6
else:
    grade = 5

# Output
print("Grade of the steel is:", grade)
