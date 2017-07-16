# In search of BITCOIN https://www.sciencedaily.com/releases/2013/02/130213225424.htm


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

num = 10000000
while True:
    if is_prime(num):
        print(num)
    num += 1
