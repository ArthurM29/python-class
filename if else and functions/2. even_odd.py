# Ask user to enter a number, check if it is an even or odd number and print the result.
#
# output should look like this:

# Please enter a number: 5
# 5 is odd number

# Please enter a number: 6
# 6 is even number

num = int(input("Please enter a number: "))

if num % 2 == 0:
    print(str(num) + " is even number")
else:
    print(str(num) + " is odd number")
