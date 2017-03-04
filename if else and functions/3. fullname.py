# Write a 'fullname()' function that accepts 2 parameters - firstname, lastname and prints fullname.
# Ask user to enter firstname and lastname and call fullname() function for these values.

# output should look like this:

# Enter your first name: Paruyr
# Enter your last name: Sevak
# Your fullname is : Paruyr Sevak


def full_name(f_name, l_name):
    print("Your fullname is : " + f_name + ' ' + l_name)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name(first_name, last_name)



