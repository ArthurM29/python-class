import openpyxl
import math
import random


class Computer:
    cities_countries = {}

    def __init__(self):
        """
        load the excel file with DB, read the data and return dictionary where:
        key = letter
        value = list of tuples, where tuple =  (city, country)
        """
        cities_db_file = r'/Users/amanasyan/Documents/Python-projects/python-class/cities/cities_DB.xlsx'
        cities_wb = openpyxl.load_workbook(cities_db_file)
        sheet = cities_wb.get_sheet_by_name('Cities_and_countries')
        # convert the generator to list to avoid “'generator' object is not subscriptable” error on openpyxl 2.3.4
        rows = list(sheet.rows)
        for row in rows:
            city, country = row[0].value, row[1].value
            first_letter = city[0]
            if first_letter not in self.cities_countries:
                self.cities_countries[first_letter] = [(city, country)]
            else:
                self.cities_countries[first_letter].append((city, country))

    def apply_difficulty(self, level):
        level = level.lower()
        if level == 'easy':
            level_rate = 0.02  # 159 cities
        elif level == 'normal':
            level_rate = 0.1  # 744 cities
        elif level == 'hard':
            level_rate = 0.3  # 2205 cities
        for letter in self.cities_countries:
            # letter generate new length, applying difficulty level on initial length
            length_by_level = math.ceil(len(self.cities_countries[letter]) * level_rate)
            # take length_by_level random values
            self.cities_countries[letter] = random.sample(self.cities_countries[letter], length_by_level)

    def print_cities_for_letter(self, letter):
        """ print (city, country) tuples for given letter """
        print("\n{}  -  {} cities \n\n".format(letter, len(self.cities_countries[letter])))
        for couple in self.cities_countries[letter]:
            print(couple)

    def print_all_cities(self):
        """ print (city, country) tuples in computer memory, grouped by letter """
        total = 0
        for letter in self.cities_countries:
            total += len(self.cities_countries[letter])
            print("\n{}  -  {} cities \n\n".format(letter, len(self.cities_countries[letter])))
            for couple in self.cities_countries[letter]:
                print(couple)
        print("\n\nTotal - %s cities" % str(total))

    def next_city(self, prev_city, cities_in_game):
        """ pick a random (city,country) tuple, remove from the list and return """
        letter = prev_city[-1].upper()
        cities_not_in_game = []
        for city_country in self.cities_countries[letter]:
            if city_country not in cities_in_game:
                cities_not_in_game.append(city_country)
        index = random.randint(0, len(cities_not_in_game) - 1)
        new_city = cities_not_in_game.pop(index)
        cities_in_game.append(new_city)
        return new_city





