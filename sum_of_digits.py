# Ask user to enter a positive integer, count sum of digits and print out in following format:

# Enter a positive integer: 135
# Sum of digits = 9

number = int(input("Enter a positive integer: "))

digit_sum = 0
while number > 0:
    next_digit = number % 10
    digit_sum += next_digit
    number = number // 10

print("Sum of digits = " + str(digit_sum))