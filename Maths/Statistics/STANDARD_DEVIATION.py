# Std Dev = √Variance
# Square root of variance
# Std Dev = “average distance from mean”

nums = [10, 20, 30, 40]

# Mean
mean = sum(nums) / len(nums)

# Variance
sum_sq = 0
for num in nums:
    sum_sq += (num - mean) ** 2

variance = sum_sq / len(nums)

# Standard Deviation
std_dev = variance ** 0.5

print("Standard Deviation:", std_dev)