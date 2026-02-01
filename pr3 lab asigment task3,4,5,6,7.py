n = int(input())
for i in range(1, n + 1):
    print(i, end="")

print("\n")

for i in range(5, 0, -1):
    print("* " * i)
print("\n")

# Upper part
for i in range(1, 5):
    print("* " * i)

# Lower part
for i in range(3, 0, -1):
    print("* " * i)


# Input validation using while loop
while True:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))
    if start > 1 and end > start:
        break
    print("Invalid input. Try again.")

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
