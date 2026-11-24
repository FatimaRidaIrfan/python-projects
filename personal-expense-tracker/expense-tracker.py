expenses = []

while True:
    print("====Personal Expense Tracker====")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Search expenses by category")
    print("5. Delete an expense")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        try:
            amount = float(input("Enter expense amount: "))
            if amount > 0:
                category = input("Enter expense category: ")
                expenses.append({
                    "name": name,
                 "amount": amount,
                    "category": category
                })

                print("Expense added successfully!")
            else:
                print("Expense amount must be greater than zero")
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")

    elif choice == "2":
        if expenses:
            for expense in expenses:
                print(expense["name"], expense["amount"], expense["category"])
        else:
            print("No expenses found")

    elif choice == "3":
        if expenses:
            total = sum(expense["amount"] for expense in expenses)
            print("Total expenses: ", total)
        else:
            print("No expenses found")

    elif choice == "4":
        category = input("Enter category: ")
        found = False 

        for expense in expenses:
            if category.lower() == expense["category"].lower():
                found = True
                print("Expense:", expense["name"])
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
            
        if found == False:
            print("No expense found in this category")

    elif choice == "5":
        expense_name = input("Enter expense name to delete: ")
        found = False 

        for expense in expenses:
            if expense["name"] == expense_name:
                expenses.remove(expense)
                found = True
                print("Expense deleted successfully!")
                break
        if found == False:
            print("Expense not found")

    elif choice == "6":
        print("Exiting Personal Expense Tracker. Goodbye!")
        break 
    else:
        print("Invalid choice, Please try again.")