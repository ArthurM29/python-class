from random import randint

comp_dice = randint(1, 6)
print("Computer rolls the dice ...", comp_dice)
user_dice = randint(1, 6)
print("User rolls the dice ...", user_dice)

if comp_dice > user_dice:
    print("Computer wins !")
elif comp_dice < user_dice:
    print("User wins !")
else:
    print("It is a tie !")
