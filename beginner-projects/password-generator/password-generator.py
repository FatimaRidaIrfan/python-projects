import secrets
import string 

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation 
while True:
    try:
        length = int(input("Enter password length: "))
        if length > 0:
            password = ""

            for i in range(length):
                password += secrets.choice(characters)

            print(password)

        else:
            print("Password length must be greater than zero")
        

    except ValueError:
        print("Please enter a valid number: ")

    again = input("Generate another password? (yes/no): ")
    if again.lower() == "no":
        break 
    elif again.lower() == "yes":
        continue
    else:
        print("Please enter yes or no")

   