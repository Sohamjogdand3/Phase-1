# Task:- Convert vector to length = 1
# Unit vector → divide by magnitude

A = [3, 4]

# magnitude
sum_sq = 0
for num in A:
    sum_sq += num ** 2

mag = sum_sq ** 0.5

unit = []

for num in A:
    unit.append(num / mag)

print("Unit Vector:", unit)