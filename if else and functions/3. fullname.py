# Write a 'mac_email()' function that accepts 2 parameters - firstname, lastname and returns email in macadamian email format(see below).
# Ask user to enter firstname and lastname, call mac_email() function for these values and print the returned email.

# output should look like this:

# Enter your first name: Arthur
# Enter your last name: Manasyan
# Your macadamian email is: amanasyan@macadamian.com


def mac_email(f_name, l_name):
    email = f_name[0].lower() + l_name.lower() + '@macadamian.com'
    return email

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

my_email = mac_email(first_name, last_name)
print("Your macadamian email is: " + my_email)

