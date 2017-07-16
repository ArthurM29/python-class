# Write a program that says hello to the user
# Ask user to enter his name, and print text to say hello to him, printing his name in uppercase letters

# Output should like this:

# What is your name ? sevak
# Hello SEVAK !

# Use string concatenation to print - note that you need to print exclamation mark at the end, and leave spaces between the strings

name = input("What is your name ? ")
print("Hello " + name.upper() + ' !')
