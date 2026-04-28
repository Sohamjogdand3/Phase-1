nums = list(map(int, input("Enter numbers: ")))

seen = set()
result = []

for num in nums:
    if num not in seen:
        result.append(num)
        seen.add(num)

print("List without duplicates:", result)