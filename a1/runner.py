from handler import *
from hill_climbing import HillClimbing

def sequel_cost(sequel):

    costs = [cities_table.loc[sequel[i], sequel[i+1]] 
              for i in range(len(sequel)-1)]

    return sum(costs)

coordinates = get_coordinates()

cities = get_cities(coordinates)

cities_table = get_cities_table(cities)

for i in range(1):

    print("\nInit 1\n")

    climb = HillClimbing(cities, cities_table)
    print(climb)
    print("\nOperator 1:")
    print(climb.hill_climb())
    
    climb = HillClimbing(cities, cities_table)
    print("\nOperator 2:")
    print(climb.hill_climb(is_first_oper=False))
    
    climb = HillClimbing(cities, cities_table)
    print("\nRandom 1:")
    print(climb.random_hill_climb())
    
    climb = HillClimbing(cities, cities_table)
    print("\nRandom 2:")
    print(climb.random_hill_climb(is_first_oper=False))


    print("\n\nInit 2\n")

    climb = HillClimbing(cities, cities_table, is_init_2=True)
    print(climb)
    print("\nOperator 1:")
    print(climb.hill_climb())
    
    climb = HillClimbing(cities, cities_table, is_init_2=True)
    print("\nOperator 2:")
    print(climb.hill_climb(is_first_oper=False))
    
    climb = HillClimbing(cities, cities_table, is_init_2=True)
    print("\nRandom 1:")
    print(climb.random_hill_climb())
    
    climb = HillClimbing(cities, cities_table, is_init_2=True)
    print("\nRandom 2:")
    print(climb.random_hill_climb(is_first_oper=False))
