# Write 2 functions:
# add() - accepts 2 numbers, returns sum of these numbers
# subtract() - accepts 2 numbers, returns subtraction of these numbers
# multiply() - accepts 2 numbers, returns multiplication of these numbers
# divide() - accepts 2 numbers, returns division of these numbers

# then, ask user to enter 2 numbers, also, ask user to enter arithmetic operation - (+-*/)
# check what operation has entered the user, call appropriate function for the 2 numbers and print the result in a nice format:

# output should look like this:

# Enter first number: 7
# Enter second number: 4
# Enter arithmetic operation (+-*/): +
# 7 + 4 = 11


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

operation = input("Enter arithmetic operation (+-*/): ")
result = 0

if operation == '+':
    result = add(number1, number2)
elif operation == '-':
    result = subtract(number1, number2)
elif operation == '*':
    result = multiply(number1, number2)
elif operation == '/':
    result = divide(number1, number2)

print(str(number1) + ' ' + operation + ' ' + str(number2) + ' = ' + str(result))




