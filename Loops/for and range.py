# Step 1 - Write a program that asks the user for a number N and prints the sum of the numbers 1 to N

num = int(input("Enter a number: "))
my_sum = 0

for i in range(1, num + 1):
    my_sum += i

print("Sum of numbers 1 to N: " + str(my_sum))


# Step 2 - Extend the previous program also to print the product of numbers from 1 to N

num = int(input("Enter a number: "))
my_sum = 0
my_prod = 1

for i in range(1, num + 1):
    my_sum += i
    my_prod *= i

print("Sum of numbers 1 to N: " + str(my_sum))
print("Product of numbers 1 to N: " + str(my_prod))


# Step 3 - Turn each action into a function: calculate_sum() and calculate_product() and modify the program
#  to use these functions to print sum and product for number N

def calculate_sum(number):
    summary = 0
    for i in range(1, num + 1):
        summary += i
    return summary


def calculate_product(number):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

num = int(input("Enter a number: "))

my_sum = calculate_sum(num)
my_prod = calculate_product(num)

print("Sum of numbers 1 to N: " + str(my_sum))
print("Product of numbers 1 to N: " + str(my_prod))


# Step 4 - Extend the program to give user the possibility to choose between computing the sum and computing
# the product of 1,…,n - ask user to enter a new parameter - values 'sum' or 'product' and choose action based on that parameter.

def calculate_sum(number):
    summary = 0
    for i in range(1, num + 1):
        summary += i
    return summary


def calculate_product(number):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

num = int(input("Enter a number: "))
option = input("Please enter action to calculate - sum/product: ")

if option == 'sum':
    my_sum = calculate_sum(num)
    print("Sum of numbers 1 to N: " + str(my_sum))
elif option == 'product':
    my_prod = calculate_product(num)
    print("Product of numbers 1 to N: " + str(my_prod))
else:
    print("You have entered invalid option\n")


# Step 5 - Extend the program to work properly even if user enters uppercase value for option
def calculate_sum(number):
    summary = 0
    for i in range(1, num + 1):
        summary += i
    return summary


def calculate_product(number):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

num = int(input("Enter a number: "))
option = input("Please enter action to calculate - sum/product: ").lower()

if option == 'sum':
    my_sum = calculate_sum(num)
    print("Sum of numbers 1 to N: " + str(my_sum))
elif option == 'product':
    my_prod = calculate_product(num)
    print("Product of numbers 1 to N: " + str(my_prod))
else:
    print("You have entered invalid option\n")