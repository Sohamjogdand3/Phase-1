# Task:- Find length of vector
# Formula:- √(x² + y² + z²)

A = [3, 4]

sum_sq = 0

for num in A:
    sum_sq+= num**2

magnitude = sum_sq **0.5

print("Vector Magnitude is: ", magnitude)