# Calculate discount

def calculate_discount(age, amount):
    discount= 0

    # Age-Based Discount
    if age < 18:
        discount += 10

    elif age >= 60:
        discount += 20

    # Purchase-based discount
    if amount > 5000:
        discount += 5

    return discount

def final_price(amount, discount):
    return amount - (amount * discount / 100)      


age = int(input("Enter your age: "))
amount = float(input("Enter purchase amount: "))

discount = calculate_discount(age, amount)
price = final_price(amount, discount)

print("Total Discount:", discount, "%")
print("Final Price:", price)  