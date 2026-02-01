import numpy as np

# Create 4x4 identity matrix
identity_matrix = np.identity(4)

print("4x4 Identity Matrix:")
print(identity_matrix)

print("\n")

import numpy as np

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Matrix Addition:")
print(A + B)

print("Matrix Multiplication:")
print(np.dot(A, B))
