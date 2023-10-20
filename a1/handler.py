#from city import city
#from hill_clibing import hill_clibing

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

    coordinates = [[x_coordinates[i], y_coordinates[i]] for i in range(len(x_coordinates))]

    return coordinates
