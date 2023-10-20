#from city import city
#from hill_clibing import hill_clibing

def get_coordinates(file_name="test.txt"):
    file = open(file_name, "r")

    x_coordinates = file.readline().split()
    y_coordinates = file.readline().split()

    x_coordinates = [float(i) for i in x_coordinates]
    y_coordinates = [float(i) for i in y_coordinates]

    return x_coordinates, y_coordinates
