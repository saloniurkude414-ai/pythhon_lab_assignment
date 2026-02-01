
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(1, 6):
    print(str(i) * i)

for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j % 2, end="")
    print()


num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()

for i in range(1, 6):
    print("*" * i)
