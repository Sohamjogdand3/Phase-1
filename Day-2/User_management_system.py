#store user from list
users=[]

#set-- for email(bcoz it allows unique value no duplicates)
emails = set()

#tuple-- for role
Roles=("admin", "user")

def add_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    role = input("Enter your Role: ")

    if role not in Roles:
        print("Invalid Role\n")
        return
    
    if email in emails:
        print("User already exist\n")
        return
    
    user = {
        "name" : name,
        "email" : email,
        "role" : role
    }

    users.append(user)
    emails.add(email)

    print("User added succesfully")

def show_users():
    if not users:
        print("No user found")
        return
    
    print("\nShow all Users")
    for user in users:
        print(user)

def main():
    while True:
        print("\n1: Add User")
        print("2: Show all Users")
        print("3: Exit")

        choice = input("Enter Choice: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


main()    