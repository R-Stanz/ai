from handler import *
from hill_climbing import HillClimbing

coordinates = get_coordinates()

cities = get_cities(coordinates)

cities_table = get_cities_table(cities)

for i in range(1):

    print("\nInit 1\n")

    climb = HillClimbing(cities, cities_table)
    print("climb:", climb)
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
