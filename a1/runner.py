from handler import *
from hill_climbing import HillClimbing

coordinates = get_coordinates()

cities = get_cities(coordinates)

cities_table = get_cities_table(cities)

climb = HillClimbing(cities, cities_table)
print(climb)
print(climb.hill_climb())
