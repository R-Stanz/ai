from handler import *

coordinates = get_coordinates()

cities = get_cities(coordinates)

cities_table = get_cities_table(cities)

cities_names = get_cities_names(cities)

print("Default MST (Including First City): \n")
for city in cities_names:

    print("First City As ", city)

    result = a_star(cities_names, cities_table, city)
    last_state, max_queue_len, last_queue_len, steps_count = result 

    print(last_state)
    print(f"Max Size Queue Of States: {max_queue_len:.4E}" \
            f"\tLast Size Queue Of State: {last_queue_len:.4E}")

print("\n\nModified MST (Not Including First City): \n")
for city in cities_names:

    print("First City As ", city)

    result = a_star(cities_names, cities_table, city, with_default_mst=False)
    last_state, max_queue_len, last_queue_len, steps_count = result 

    print(last_state)
    print(f"Max Size Queues Of States: {max_queue_len:.4E}" \
            f"\tLast Size Queue Of State: {last_queue_len:.4E}")
