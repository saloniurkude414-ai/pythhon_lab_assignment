import numpy as np

print("Enter elements of 5x3 matrix:")
A = np.zeros((5, 3), dtype=int)
for i in range(5):
    for j in range(3):
        A[i][j] = int(input())

print("Enter elements of 3x2 matrix:")
B = np.zeros((3, 2), dtype=int)
for i in range(3):
    for j in range(2):
        B[i][j] = int(input())

C = np.dot(A, B)

print("Product Matrix:")
print(C)
