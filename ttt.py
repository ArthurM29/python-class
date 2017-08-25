name = input("Please enter any name: ")
length_name = len(name)

if length_name > 0 and length_name <= 4:
    print("Wow, " + name + ", kudos to your parents for a short name that's easy to pronounce !!! ")
elif length_name > 4 and length_name < 8:
    print("Well, " + name + ", you have a middle-length name")
else:
    print(name + ", my dear, your name is way too long, we need to think of a nickname for you buddy !!!")
#Part 2
    if name[2] is "a" or name[2] is "e" or name[2] is "i" or name[2] is "o" or name[2] is "u":
        print("Let's call you " + name[0:2] + "o :D :D :D")
    else:
        print("Let's call you " + name[0:3] + "o :D :D :D")


# x = 'a'
# if 'aa' is x*2:
#     print(True)