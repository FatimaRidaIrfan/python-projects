a = float(input("Enter 1st Number:"))
b = float(input("Enter 2nd Number:"))
operation = input("Enter the operation:(+, -, *, /, **, %)")

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a-b)
elif operation == '*':
    print(a*b)
elif operation == '/':
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
elif operation == '**':
    print(a**b)
elif operation == '%':
    if b != 0:
        print(a % b)
    else:
        print("Cannot calculate modulus with zero")

else:
    print("INVALID OPERATION")

