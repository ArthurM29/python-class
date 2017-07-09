# Declare a variable and store user's 'dirty' salary - 250000
# Declare another variable and store the tax_rate - 25.7
# Calculate his clean salary (without tax) and print out in following format:

# Clean salary - 185750.0

dirty_salary = 250000
tax_rate = 25.7
tax = dirty_salary / 100 * tax_rate
clean_salary = dirty_salary - tax
print('Clean salary - ' + str(clean_salary))
