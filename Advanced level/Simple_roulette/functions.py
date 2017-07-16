# create a game


import random
import time


def spin_the_wheel():
    """ choose an option from ['red', 'black'], print the result and return it """
    options = ['black', 'red']
    print("Spinning the wheel ... ", flush=True, end=" ")   # by default console output is buffered. use keyword argument 'flush'
    time.sleep(2)
    result = random.choice(options)
    print("It is %s!" % result.title())   # start with uppercase
    return result


def place_a_bet(balance):
    """ keep asking user to enter bet_amount and bet_option until he enters valid values and return them """
    while True:
        bet_amount = int(input("Place a bet: "))
        if 0 < bet_amount <= balance:
            break
        else:
            print("Please place a bet between 0 and your balance\n")

    while True:
        bet_option = input("Red or black? ").lower()
        if bet_option in ['black', 'red']:
            break
        else:
            print("Please place your bet on Red or Black\n")
    return bet_amount, bet_option


def update_balance(balance, bet_option, bet_amount, result):
    """ update the balance based on result and return updated balance """
    if bet_option == result:
        print("You won ${}".format(2 * bet_amount))
        balance += 2 * bet_amount
    else:
        print("You lost ${}".format(bet_amount))
        balance -= bet_amount
    return balance
