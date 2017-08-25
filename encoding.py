#  You are given a string which is encoded using a siple algorithm:   'sggkh://ddd.blfgfyv.xln/dzgxs?e=ut2BS7H_wAU'

# write a program to decode the string. Use these 2 strings:

#  letters = 'abcdefghijklmnopqrstuvwxyz'
#  encoding_str = 'zyxwvutsrqponmlkjihgfedcba'

import string
letters = string.ascii_lowercase
encoding_str = letters[::-1]
print(letters)
print(encoding_str)


def encode(initial_str, encoding):
    encoded_str = ''
    for char in initial_str:
        if char in letters:
            index = letters.index(char)
            encoded_str += encoding[index]
        else:
            encoded_str += char
    return encoded_str


def decode(initial_str, encoding):
    decoded_str = ''
    for char in initial_str:
        if char in encoding:
            index = encoding.index(char)
            decoded_str += letters[index]
        else:
            decoded_str += char
    return decoded_str

my_string = 'https://www.youtube.com/watch?v=fg2BS7H_dAU'
encoded_string = encode(my_string, encoding_str)
print(encoded_string)
decoded_string = decode(encoded_string, encoding_str)
print(decoded_string)