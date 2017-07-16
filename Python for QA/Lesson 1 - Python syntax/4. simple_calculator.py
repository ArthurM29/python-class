# Write a program that calculates arithmetic operations on integer numbers

# declare 2 variables and assign integer numbers to these variables
# calculate and print out the following values:
# sum
# difference
# product
# quotient
# integer division
# remainder of division from first number on the second
# exponent(power) X^y

# Note: use the following format to print text and numbers on the same line:
# print("age = " + str(64))   - put your variable instead of 64

# test your program with following test cases and make sure your program prints the same values in the same format:

# test case 1: for numbers num1 = 11 and num2 = 5 the program print following output:

# sum = 16
# difference = 6
# product = 55
# quotient = 2.2
# integer division = 2
# remainder = 1
# exponent = 161051


number1 = 11
number2 = 5

sum = number1 + number2
print("sum = " + str(sum))

difference = number1 - number2
print("difference = " + str(difference))

product = number1 * number2
print("product = " + str(product))

quotient = number1 / number2
print("quotient = " + str(quotient))

int_division = number1 // number2
print("integer division = " + str(int_division))

remainder = number1 % number2
print("remainder = " + str(remainder))

exponent = number1 ** number2
print("exponent = " + str(exponent))