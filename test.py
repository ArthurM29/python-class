def mac_email(first_name, last_name):
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")
    email = "Your macadamian email is:" + str.lower(first_name[0]) + str.lower(last_name) + "@macadamian.com"
    print(email)

#let's discuss why I should create function
mac_email("fname", "lname")




# move data input out of function definition