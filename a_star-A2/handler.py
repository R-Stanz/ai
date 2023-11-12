from city import City
import pandas as pd

def get_coordinates(file_name="test.txt"):

    try:
        file = open(file_name, "r")

        x_coordinates = file.readline().split()
        y_coordinates = file.readline().split()
        
        file.close()

    except Exception as exc:
        raise OSError("Something went wrong while reading" \
                        "the file!") from exc

    x_coordinates = [float(i) for i in x_coordinates]
    y_coordinates = [float(i) for i in y_coordinates]

    rate = len(x_coordinates) / len(y_coordinates)
    if(rate != 1):
        raise IndexError("The rate for the coordinates in each axis isn't 1. Rate: ", rate)

    coordinates = [(x_coordinates[i], y_coordinates[i]) for i in range(len(x_coordinates))]

    return coordinates


def get_cities(coordinates):

    cities  = []
    count   = 0
    for coordinate in coordinates:

        city_name= get_city_name(count)
        count   += 1

        cities  += [City(city_name, coordinate)]

    return cities


def get_city_name(city_numb):

    name = ""

    numb_of_As = city_numb // 52
    for i in range(numb_of_As):
        name += chr(65)

    city_numb %= 52
    if(city_numb < 26):
        name += chr(city_numb + 65)
    else:
        name += chr(city_numb - 26 + 97)

    return name


def get_cities_table(cities):

    data =  [dict(  
                    (
                        cities[j].name,
                        get_distance(cities[i], cities[j])
                    )
                    for j in range(len(cities))
                 )

                for i in range(len(cities))
             ]

    cities_df = pd.DataFrame(data, index=[i.name for i in cities])
    pd.set_option('display.float_format', '{:.4E}'.format)

    return cities_df


def get_distance(city_1, city_2):

    distance = ((city_1.x_axis - city_2.x_axis)**2 
                + (city_1.y_axis - city_2.y_axis)**2)**(1/2)

    return distance


def get_cities_names(cities):
    return [city.name for city in cities]
