# Task:- If dot product = 0 → perpendicular
# Orthogonal → dot product = 0

A = [1, 0]
B = [0, 1]

dot = 0

for i in range(len(A)):
    dot += A[i] * B[i]

if dot == 0:
    print("Orthogonal")
else:
    print("Not Orthogonal")