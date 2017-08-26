class Player:
    def next_city(self, prev_city, cities_in_game):
        letter = prev_city[-1].upper()
        city = ''
        while not city:
            city = input("Enter a city: ").title()
            if city.startswith(letter):
                if city not in cities_in_game:
                    cities_in_game.append(city)
                    return city
                else:
                    print("That city has already been mentioned during this game, find another one !")
                    city = ''
            else:
                print("You should enter a city starting with letter %s" % letter)
                city = ''
