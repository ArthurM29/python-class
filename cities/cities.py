# can I read from file on condition ?
# who is the winner and how to end the game ?


from functions import load_cities_db, next_city, new_city_is_valid, apply_difficulty
import sys


cities_and_countries_by_letter = load_cities_db()
cities_in_game = []
level = input("Enter difficulty - easy/normal/hard: ")
apply_difficulty(cities_and_countries_by_letter, level)

# sum = 0
# for letter in cities_and_countries_by_letter:
#     print('{}   : {}'.format(letter, len(cities_and_countries_by_letter[letter])))
#     print(4 * '\n')
#     sum += len(cities_and_countries_by_letter[letter])
#     for city,country in cities_and_countries_by_letter[letter]:
#         print("{} : {}".format(city, country))
#
# print("Total - " + str(sum))


user_city = input("Enter a city: ")

while user_city != 'end'.lower():
    last_letter = user_city[-1].upper()
    while True:
        if set(cities_and_countries_by_letter[last_letter]) == set(cities_in_game):
            print("Computer has ran out of cities. You won !!!")
            sys.exit(0)
        pc_city, pc_country = next_city(cities_and_countries_by_letter[last_letter])
        if new_city_is_valid(last_letter, pc_city, cities_in_game):
            break
    print("Computer said: {:<30} (city in {})".format(pc_city, pc_country), '\n')
    last_letter = pc_city[-1]
    while True:
        user_city = input("Enter a city: ")
        if new_city_is_valid(last_letter, user_city, cities_in_game):
            break


