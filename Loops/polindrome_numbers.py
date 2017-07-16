# number = int(input("Enter a number: "))


def is_palindrome(num):
    digits = str(num)
    for i in range(len(digits) // 2):
        if digits[i] != digits[-(i + 1)]:
            return False
    return True

# if is_palindrome(number):
#     print("{} is a palindrome".format(number))
# else:
#     print("{} is not a palindrome".format(number))


for i in range(1000, 1000000):
    if is_palindrome(i):
        print(i)