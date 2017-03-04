# Accept 5 integer numbers from user input, keep them in a list. For each number, define if it is even or odd,
# print the number and a text informing if the number is even or odd.

numbers = []

for i in range(5):
    num = int(input())
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is an even number")
    else:
        print(str(num) + " is an odd number")
