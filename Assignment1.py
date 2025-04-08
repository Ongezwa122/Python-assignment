# Simple calculator program

# Ask the user to input the first number second number and operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /):")

# Perform the operation and print the result
if operation == '+':
    result = num1 + num2
    print(round(result, 3))
elif operation == '-':
    result = num1 - num2
    print(round(result, 3))
elif operation == '*':
    result = num1 * num2
    print(round(result, 3))
elif operation == '/':
    result = num1 / num2
    print(round(result, 3))
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
