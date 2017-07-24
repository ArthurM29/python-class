import openpyxl
from random import choice, sample
import math
import sys


def load_cities_db():
    """
    load the excel file with DB, read the data and return dictionary where:
    key = letter
    value = list of tuples, where tuple =  (city, country)
    """
    cities_db_file = r'/Users/amanasyan/Documents/Python projects/python-class/cities/cities_DB.xlsx'
    cities_wb = openpyxl.load_workbook(cities_db_file)
    sheet = cities_wb.get_sheet_by_name('Cities_and_countries')
    rows = list(sheet.rows)   # convert the generator to list to avoid “'generator' object is not subscriptable” error on openpyxl 2.3.4
    cities_and_countries_by_letter = {}
    for row in rows:
        city = row[0].value
        country = row[1].value
        first_letter = city[0]
        if first_letter not in cities_and_countries_by_letter:
            cities_and_countries_by_letter[first_letter] = [(city, country)]
        else:
            cities_and_countries_by_letter[first_letter].append((city, country))
    return cities_and_countries_by_letter


def next_city(cities_and_countries):
    """ receive a list of (city, country) tuples, where city starts with specified letter and return a random one """
    return choice(cities_and_countries)


def new_city_is_valid(letter, city, cities_in_game):
    # turn strings to uppercase to have correct comparisons
    letter = letter.upper()
    city = city.upper()
    if city.startswith(letter):
        if city not in cities_in_game:
            cities_in_game.append(city)
            return True
        else:
            print("That city has already been mentioned during this game, find another one :)")
    else:
        print("You should enter a city starting with letter %s" % letter)
    return False


def apply_difficulty(cities_and_countries_by_letter, level):
    level = level.lower()
    if level == 'easy':
        level_rate = 0.02   # 133 cities
    elif level == 'normal':
        level_rate = 0.1    # 719 cities
    elif level == 'hard':
        level_rate = 0.3    # 2180 cities

    for letter in cities_and_countries_by_letter:
        length_by_level = math.ceil(len(cities_and_countries_by_letter[letter]) * level_rate)
        cities_and_countries_by_letter[letter] = sample(cities_and_countries_by_letter[letter], length_by_level)





















