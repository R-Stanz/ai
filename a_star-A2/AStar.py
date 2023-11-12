import random as rnd
from Node import Node

class AStar:
    def __init__(self, cities, cost_table):

        self.cities         = cities
        self.cost_table     = cost_table

    def run(self):

        first_node   = Node(self.cities, self.cities[0], self.cost_table)
        self.nodes   = [first_node]
        current_node = None

        while (current_node != first_node):

            if (len(nodes) = 0):
                self.nodes = [Node(cities)]

            current_node     = self.nodes.pop(0)
            new_nodes        = current_node.get_children()

            if (len(new_nodes) == 0):
                new_nodes += [first_node]

            self.nodes      += new_nodes
            self.nodes.sort(key=lambda node: node.get_path_cost() + node.get_mst(first_node))
