for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

for i in range(1, 5):
    print("# " * i)



letters = ['p', 'y', 't', 'h', 'o']
for i in range(len(letters)):
    print(letters[i] * (i + 1))


word = "python"
for i in range(1, len(word) + 1):
    print(word[:i])
