
# Tricky case: letter has multiple occurrences in the word

from functions import open_letter, import_questions
from random import choice
import math

questions_answers = import_questions()
question = choice(list(questions_answers))
answer = questions_answers[question]
ATTEMPTS = math.ceil(len(answer) / 2)
guess_word = len(answer) * '*'
print(question, ': ', guess_word)

while guess_word != answer and ATTEMPTS > 0:
    guess = input("\nEnter a letter or guess the word: ").upper()
    # if user guessed the word, exit the game
    if guess == answer:
        print("Correct ! You guessed the word !!!  %s" % answer)
        break
    # if user hasn't guessed the word, check the guessed letter
    if len(guess) == 1 and guess in answer:  # only one letter guess
        guess_word = open_letter(answer, guess, guess_word)
        print(guess_word)
        if guess_word == answer:
            print("Correct ! You guessed the word !!!  %s" % answer)
    else:
        print("Your guess is wrong !")
        ATTEMPTS -= 1
        print("%s attempts left" % ATTEMPTS)
        if ATTEMPTS == 0:
            print("You ran out of attempts. You lost the game.")





