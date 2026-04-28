# Variance = Σ (x - mean)² / n
# Variance = “How spread out the data is”
# Variance = medium
''' Steps:

Find mean
Subtract mean from each value
Square it
Average it '''

nums = [10, 20, 30, 40]

# Step 1: Mean
total = 0
for num in nums:
    total += num
mean = total / len(nums)

# Step 2–4: Variance
sum_sq_diff = 0

for num in nums:
    diff = num - mean
    sum_sq_diff += diff ** 2

variance = sum_sq_diff/ len(nums)

print("mean: ", mean)
print("Variance", variance)