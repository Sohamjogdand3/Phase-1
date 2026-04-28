# The middle value after sorting data
''' 
Steps
Sort data
If odd → middle value
If even → average of two middle values
'''

nums = [10,20,30,40,50]

nums.sort()

n=len(nums)

if n% 2 == 1:
    median = nums[n//2]
else:
    median = (nums[n//2 - 1] + nums[n//2]) / 2

print("Median:", median)        