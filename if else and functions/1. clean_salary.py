# Ask user to enter his dirty salary, calculate his clean salary and print (count tax rate as 25.7%)
#
# output should look like this:

# Please enter your dirty salary: 200000
# Clean salary = 148600.0

tax_rate = 25.7
dirty_salary = int(input("Please enter your dirty salary: "))
tax = dirty_salary / 100 * tax_rate
clean_salary = dirty_salary - tax
print("Clean salary = " + str(clean_salary))
