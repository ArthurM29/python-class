# Write a program that generates an abbreviation (acronym) from a string.

# test your program with following test cases:

# case 1: when text = No Problem, abbreviation = NP
# case 2: when text = Working from home, abbreviation = WFH
# case 3: when text = north atlantic treaty organization, abbreviation = NATO


text = input("Enter a string: ")
acronym = ''
words = text.split()
for word in words:
    acronym += word[0].upper()

print(acronym)
