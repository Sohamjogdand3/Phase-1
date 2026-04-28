List1= list(map(int,input("Enter First List: ")))
List2= list(map(int,input("Enter Second List: ")))

merged_list = List1 + List2
merged_list.sort()

print("Merged & Sorted List:", merged_list)