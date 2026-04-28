# Mean = (x₁ + x₂ + x₃ + ... + xₙ) / n
# sum of all values divided by total count
# Mean = “center value”

nums = [10, 20, 30, 40, 50]

total = 0

for num in nums:
    total += num

mean = total/ len(nums)

print("Mean Value: ", mean)