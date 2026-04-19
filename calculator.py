#Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

#Ask for operation
if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result):", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")

elif operation == "**":
    print("Result:", num1 ** num2)
else:
    print("Invalid operation")