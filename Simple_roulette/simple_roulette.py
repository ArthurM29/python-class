from Simple_roulette.functions import spin_the_wheel, place_a_bet, update_balance

balance = 100

while balance > 0:
    print("Your balance is $%s\n" % balance)
    bet_amount, bet_option = place_a_bet(balance)
    result = spin_the_wheel()
    balance = update_balance(balance, bet_option, bet_amount, result)
    if balance <= 0:
        print("You've lost all your money. Go home now.")
        break











