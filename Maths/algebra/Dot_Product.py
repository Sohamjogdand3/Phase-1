# Dot Product = Multiply and sum

A = [1, 2, 3]
B = [4, 5, 6]

dot = 0

for i in range(len(A)):
    dot += A[i]*B[i]

print("Dot Product: ", dot)