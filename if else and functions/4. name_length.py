# Part 2: Write 'name_length()' function that accepts name as parameter, counts its length, checks for 3 conditions:
# if name length is in interval (0, 4]  - print that it is a short name.
# if name length is in interval (4, 8)  - print that it is a middle length name.
# if name length is in longer than 8  - print that it is a long name.
# Ask user to enter a name and call name_length function for entered name.

# for the text and format how to print see below samples for output

# Enter your name: Gor
# Wow, Gor, kudos to your parents for a short name that's easy to pronounce !!!

# Enter your name: Armen
# Well, Armen, you have a middle-length name

# Enter your name: Varazdat
# Varazdat, my dear, your name is way too long, we need to think of a nickname for you buddy !!!


# Part 2: for the case when name length > 8, modify the code to construct a short name by taking first 5 characters of
# his/her name and print it to user

# output should look like this:

# Enter your name: Varazdat
# Varazdat, my dear, your name is way too long, we need to think of a nickname for you buddy !!!
# Let's call you Varaz

# hint: user string slicing
# e.g.
# s = 'Sanasar'
# s = s[:3] + s[3:]
# s[2:5] = 'nas'    from 2nd inclusive to 5th exclusive
# s[:5] = 'sanas'   from start up to 5th exclusive
# s[2:] = 'nasar'   from 2nd element up to end


def name_length(my_name):
    if 0 < len(my_name) <= 4:
        print("Wow, " + my_name + ", kudos to your parents for a short name that's easy to pronounce !!!")
    elif 4 < len(my_name) < 8:
        print("Well, " + my_name + ", you have a middle-length name")
    elif len(my_name) >= 8:
        print(my_name + ", my dear, your name is way too long, we need to think of a nickname for you buddy !!!")
        print("Let's call you " + my_name[:5])

name = input("Enter your name: ")
name_length(name)
