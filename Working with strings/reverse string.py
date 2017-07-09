# Ask user to enter a string, print out the reversed string in following format:


#Enter a string: Macadamian
#Reversed string: naimadacaM

my_str = input("Enter a string: ")
reversed_str = ''

index = len(my_str)
for i in range(len(my_str)):
    reversed_str += my_str[index - 1]
    index -= 1

print('Reversed string: ' + reversed_str)
