from handler import *
from Node import Node

coordinates = get_coordinates()

cities = get_cities(coordinates)

cities_table = get_cities_table(cities)

cities_names = get_cities_names(cities)

first_node  = Node(cities_names, cities_names[0], cities_table)
nodes       = [first_node]
current_node = None

while (current_node != first_node):

    if (len(nodes) == 0):
        nodes = [Node(cities)]

    current_node     = nodes.pop(0)
    new_nodes        = current_node.get_children()

    if (len(new_nodes) == 0):
        new_nodes += [first_node]

    nodes      += new_nodes
    nodes.sort(key=lambda node: node.get_path_cost() + node.get_mst(first_node))
