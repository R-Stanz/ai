from handler import *
from HillClimbing import HillClimbing
from DataHandler import Data

coordinates = get_coordinates()

cities = get_cities(coordinates)

cities_table = get_cities_table(cities)

data = Data()
for i in range(30):

    climb = HillClimbing(cities, cities_table)
    stats = climb.hill_climb()
    data.add_data(stats, type=1)
    
    climb = HillClimbing(cities, cities_table)
    stats = climb.hill_climb(is_first_oper=False)
    data.add_data(stats, type=2)
    
    climb = HillClimbing(cities, cities_table)
    stats = climb.random_hill_climb()
    data.add_data(stats, type=3)
    
    climb = HillClimbing(cities, cities_table)
    stats = climb.random_hill_climb(is_first_oper=False)
    data.add_data(stats, type=4)


    climb = HillClimbing(cities, cities_table, is_init_2=True)
    stats = climb.hill_climb()
    data.add_data(stats, type=5)
    
    climb = HillClimbing(cities, cities_table, is_init_2=True)
    stats = climb.hill_climb(is_first_oper=False)
    data.add_data(stats, type=6)
    
    climb = HillClimbing(cities, cities_table, is_init_2=True)
    stats = climb.random_hill_climb()
    data.add_data(stats, type=7)
    
    climb = HillClimbing(cities, cities_table, is_init_2=True)
    stats = climb.random_hill_climb(is_first_oper=False)
    data.add_data(stats, type=8)

data.basic_plot()

msg  = data.get_avg_path_size()
msg += data.get_avg_loaded()
msg += data.get_avg_final_cost()
print(msg)
