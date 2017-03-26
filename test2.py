def name_length():
    name = input(str("Enter your name:").strip())
    if len(name) in range(1, 4):
        print("Wow, {}, your name is short. Coolio".format(name)).strip()
    elif len(name) in range(4, 8):
        print(str("Hey {}, your name is middle-length".format(name)).strip())
    elif len(name) >= 8:
        print(str("{}, your name rocks. It is very long. You need a nickname honey".format(name)).strip())
        print("Let's call you", (name[0:5]))

name_length()



# Comments

# 1. move data input out of function definition

# 2. name input
# a) why do you need to convert to str ? No need.
# b) even if you needed to use str(), it is called on "Enter your name:" - doesn't make sense (remember where you placed float in first practice)
# c) why did you decide to strip() the strings ? Actually, makes sense
# d) strip is called on str("Enter your name:"), so it doesn't strip spaces from the input string

# Advice: as a beginner, avoid using too many embedded statements, use simpler code which is more readable

# 3. if len(name) in range(1, 4):
# a) can't say that using range is wrong, but not the best way to do this, on big intervals you will create long lists
# b) and it works wrong with range() - 4 length names are counted as middle instead of short
# c) why do you strip the string ?
# d) getting error on name 'Gor' - calling strip() on print instead of the string

# 4. elif len(name) in range(4, 8):
# a) Why do you use str() ?

# 5. elif len(name) >= 8:
# a) just know that you could skip 0 in name[0:5]



