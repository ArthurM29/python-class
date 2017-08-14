from string import ascii_lowercase
from random import choice
import pyperclip

string_length = int(input("Enter length of the string: "))
final_string = ''

for i in range(string_length):
    final_string += choice(ascii_lowercase)

print(final_string)
pyperclip.copy(final_string)

input("\nEnter any key to exit")





