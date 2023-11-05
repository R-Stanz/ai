import random as rnd
from Node import Node

class AStar:
    def __init__(self, cities, cost_table, mst_options):

        self.cities         = cities
        self.first_city     = cities[0]
        self.cost_table     = cost_table
        self.mst_options    = mst_options


    nodes = []
    def run(self):
        cities_order = rnd.sample(cities, len(cities))

        self.nodes  = [Node(cities)]
        next_nodes  = self.nodes[0].get_children()
        self.nodes += []
        
        node = nodes.pop(0)

    def mst(self, path):
