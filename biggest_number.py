# Ask user to enter 10 positive integers, store them in a list, then find the greatest number

numbers = []
print("Enter 10 positive integer numbers: ")

for i in range(10):
    number = int(input())
    numbers.append(number)

max_number = 0

for number in numbers:
    if number > max_number:
        max_number = number

print("Greatest number - " + str(max_number))