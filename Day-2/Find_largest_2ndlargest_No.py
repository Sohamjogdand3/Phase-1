nums = list(map(int, input("Enter numbers: ")))

largest = float('-inf')
sec_largest = float('-inf')

for num in nums:
    if num > largest:
        sec_largest = largest
        largest = num
    elif num > sec_largest and num != largest:
        sec_largest = num
        
if sec_largest == float('-inf'):
    print("No second largest element")
else:
    print("Second largest:", sec_largest)        
