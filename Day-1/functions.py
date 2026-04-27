def get_marks():
    maths = int(input("Enter your maths marks out of 100: "))
    science = int(input("Enter your science marks out of 100: "))
    english = int(input("Enter your english marks out of 100: "))
    marathi = int(input("Enter your marathi marks out of 100: "))
    return maths + science + english + marathi


def calculate_avg(total):
    return total / 4


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"


total = get_marks()
avg = calculate_avg(total)
g = grade(avg)   

print("Total:", total)
print("Average:", avg)
print("Grade:", g)