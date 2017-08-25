# Write a program that prompts user to enter his firstname and lastname, constructs email
# in macadamian email format and prints out. Examples for macadamian email format: amananasyan@macadamian.com
# Though user is expected to enter his firstname and lastname in uppercase, make sure final email is in lowercase letters.

# output should look like this:

# Enter your first name: Arthur
# Enter your last name: Manasyan
# Your macadamian email is: amanasyan@macadamian.com


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = first_name[0].lower() + last_name.lower() + '@macadamian.com'
print("Your macadamian email is: " + email)
