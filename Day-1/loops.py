count = 0
total = 0
even_count = 0
odd_count = 0

while True:
    user_input = input("Enter a number (-1 to stop): ")

    # Handle empty input
    if user_input == "":
        print("Please enter a number!")
        continue

    num = int(user_input)

    if num == -1:
        break

    if num < 1:
        continue

    count += 1
    total += num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1  

print("--RESULT--") 
print("Total numbers entered:", count)
print("Sum:", total)

if count > 0:
    print("Average:", total / count)

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)