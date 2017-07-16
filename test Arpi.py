def calculate(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    return result

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

operation = input("Enter arithmetic operation (+-*/): ")
res = calculate(number1, number2, operation)
print(res)