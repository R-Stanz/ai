from handler import *
from HillClimbing import HillClimbing

coordinates = get_coordinates()

cities = get_cities(coordinates)

cities_table = get_cities_table(cities)

for i in range(1):

    print("\nInit 1\n")

    climb = HillClimbing(cities, cities_table)
    print("climb:", climb)
    print("\nOperator 1:")
    climb.hill_climb()
    print(climb)
    
    climb = HillClimbing(cities, cities_table)
    print("\nOperator 2:")
    climb.hill_climb(is_first_oper=False)
    print(climb)
    
    climb = HillClimbing(cities, cities_table)
    print("\nRandom 1:")
    climb.random_hill_climb()
    print(climb)
    
    climb = HillClimbing(cities, cities_table)
    print("\nRandom 2:")
    climb.random_hill_climb(is_first_oper=False)
    print(climb)


    print("\n\nInit 2\n")

    climb = HillClimbing(cities, cities_table, is_init_2=True)
    print("\nOperator 1:")
    climb.hill_climb()
    print(climb)
    
    climb = HillClimbing(cities, cities_table, is_init_2=True)
    print("\nOperator 2:")
    climb.hill_climb(is_first_oper=False)
    print(climb)
    
    climb = HillClimbing(cities, cities_table, is_init_2=True)
    print("\nRandom 1:")
    climb.random_hill_climb()
    print(climb)
    
    climb = HillClimbing(cities, cities_table, is_init_2=True)
    print("\nRandom 2:")
    climb.random_hill_climb(is_first_oper=False)
    print(climb)
