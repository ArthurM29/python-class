# can I read from file on condition ?

from functions import load_cities_db, next_city, new_city_is_valid, apply_difficulty, pc_has_lost, print_cities
import sys


cities_countries = load_cities_db()
cities_in_game = []
level = input("Enter difficulty - easy/normal/hard: ")
apply_difficulty(cities_countries, level)

# use this for testing difficulty
#print_cities(cities_countries)

user_city = '__start__'

while user_city != 'resign'.lower():
    last_letter = user_city[-1]
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



