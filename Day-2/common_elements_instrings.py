str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

set1 = set(str1)
set2 = set(str2)

common = set1 & set2 

if common:
    print("Common elements:", common)
else:
    print("No common elements")