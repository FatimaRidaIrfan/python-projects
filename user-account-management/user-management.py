users = []

while True:
    print("\n====User Account Management====")
    print("1. Register a new user")
    print("2. View all users")
    print("3. Search for a user")
    print("4. Update user details")
    print("5. Delete a user")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter your username: ")
        role = input("Enter your role (Admin or User): ")
        role = role.lower()

        if role == "admin" or role == "user":
            found = False 
            for user in users:
                if user["username"] == username:
                    found = True 
            if found == False:
                    users.append({"username": username, "role": role})
                    print("User registered successfully!")
            else:
                print("Username already exists")
        else:
            print("Invalid role")

    elif choice == "2":
        if users:
            for user in users:
                print("Username:",user["username"])
                print("Role:", user["role"])
        else:
            print("No user exists")

    elif choice == "3":
        search_username = input("Enter your username: ")
        found = False 

        for user in users:
            if user["username"] == search_username:
                found = True
                print(user["username"], user["role"])

        if found == False:
            print("User not found")

    elif choice == "4":
        update_details = input("Update your details: ")
        found = False

        for user in users:
            if user["username"] == update_details:
                found = True

                new_role = input("Enter the new role (Admin or User): ")
                new_role = new_role.lower()

                if new_role == "admin" or new_role == "user":
                    user["role"] = new_role
                    print("User details updated successfully!")
                else:
                    print("Invalid role")

            if found == False:
                print("User not found")

    elif choice == "5":
        username = input("Enter username to delete: ")
        found = False 

        for user in users:
            if user["username"] == username:
                users.remove(user)
                found = True 
                print("User deleted successfully!")
                break
        if found == False:
            print("User not found")

    elif choice == "6":
        print("Exiting User Account Management System. Goodbye!")
        break
    else:
        print("Invalid choice")

