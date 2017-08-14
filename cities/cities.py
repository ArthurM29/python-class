# can I read from file on condition ?


from functions import load_cities_db, next_city, new_city_is_valid, apply_difficulty, pc_has_lost
import sys


cities_countries = load_cities_db()
cities_in_game = []
level = input("Enter difficulty - easy/normal/hard: ")
apply_difficulty(cities_countries, level)

sum = 0
for letter in cities_countries:
    print('{}   : {}'.format(letter, len(cities_countries[letter])))
    print(4 * '\n')
    sum += len(cities_countries[letter])
    for city, country in cities_countries[letter]:
        print("{} : {}".format(city, country))

print("Total - " + str(sum))
user_city = '__start__'

while user_city != 'end'.lower():
    user_city = ''
    last_letter = user_city
    while not new_city_is_valid(last_letter, user_city, cities_in_game):
        user_city = input("Enter a city: ")
    last_letter = user_city[-1].upper()

    while True:
        if pc_has_lost(cities_countries[last_letter], cities_in_game):
            print("Computer has ran out of cities. You won !!!")
            sys.exit(0)
        pc_city, pc_country = next_city(cities_countries[last_letter])
        if new_city_is_valid(last_letter, pc_city, cities_in_game):
            break
    print("Computer said: {:<30} (city in {})".format(pc_city, pc_country), '\n')
    last_letter = pc_city[-1]



