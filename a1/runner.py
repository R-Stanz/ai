from handler import *
from hill_climbing import HillClimbing

def sequel_cost(sequel):

    costs = [cities_table.loc[sequel[i], sequel[i+1]] 
              for i in range(len(sequel)-1)]

    return sum(costs)

coordinates = get_coordinates()

cities = get_cities(coordinates)

cities_table = get_cities_table(cities)

print("\nInit 1\n")
climb = HillClimbing(cities, cities_table)
print(climb)
print("\nOperator 1:")
print(climb.hill_climb())
climb = HillClimbing(cities, cities_table)
print("\nOperator 2:")
print(climb.hill_climb(False))
climb = HillClimbing(cities, cities_table)
print("\nRandom 1:")
print(climb.random_hill_climb())
climb = HillClimbing(cities, cities_table)
print("\nRandom 2:")
print(climb.random_hill_climb(False))
