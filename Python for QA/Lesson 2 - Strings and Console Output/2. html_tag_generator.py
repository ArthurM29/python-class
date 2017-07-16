# Write a program to generate HTML tags
# Ask user to enter a string, then create an HTML tag with that string and print out - use string formatting with %

# test your program with following test cases:

# case 1: when user enters = div, HTML tag = <div></div>
# case 2: when user enters = body, HTML tag = body></body>

user_str = input("Enter a string: ")
print("<%s></%s>" % (user_str, user_str))
