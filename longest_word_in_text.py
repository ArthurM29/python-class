# Declare a string with following text:
# "Failure is an option here. If things are not failing, you are not innovating enough. Elon Musk"
# find the longest word in the text and print in following format:

# Longest word - innovating
# Length - 10

quote = "Failure is an option here. If things are not failing, you are not innovating enough. Elon Musk"

words = quote.split()
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word - " + longest_word)
print("Length - " + str(len(longest_word)))
