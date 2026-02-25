def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed!"

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Modulus by zero not allowed!"

while True:
    print("\n---- CALC MENU ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice in [1, 2, 3, 4, 5]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", add(num1, num2))
    elif choice == 2:
        print("Result =", subtract(num1, num2))
    elif choice == 3:
        print("Result =", multiply(num1, num2))
    elif choice == 4:
        print("Result =", divide(num1, num2))
    elif choice == 5:
        print("Result =", modulus(int(num1), int(num2)))
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")