# Write a program that calculates user's clean salary

# declare a variable and store user's 'dirty' salary - 250000
# declare another variable and store the tax_rate - 25.7
# calculate his clean salary (without tax) and print out the clean salary: 185750.0

# test your program with following test cases:

# case 1: when dirty salary = 120000, clean salary = 89160.0
# case 2: when dirty salary = 500000, clean salary = 371500.0

dirty_salary = 250000
tax_rate = 25.7
tax = dirty_salary / 100 * tax_rate
clean_salary = dirty_salary - tax
print(clean_salary)
