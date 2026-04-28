# The value that appears most frequently
# Mode = “most common value”

nums = [1, 2, 2, 3, 4, 2, 5]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

mode = max(freq, key=freq.get)

print("Mode:", mode)