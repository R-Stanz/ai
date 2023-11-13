class Node:

    def __init__(self, cities, node_city, cost_table, previous_node=None):
        self.cities         = cities
        self.cost_table     = cost_table
        self.previous_node  = previous_node
        self.node_city      = node_city


    def __str__(self):
        msg = "Path: " 

        path = self.get_path()

        for city in path:
            msg += city

        cost = self.get_path_cost()
        msg += f"\nPath cost: {cost:.4E}"

        return msg


    def get_path(self):
        tmp_node        = self
        city            = self.node_city
        reverse_path    = [city]

        while (tmp_node.previous_node != None):
            tmp_node         = tmp_node.previous_node
            city             = tmp_node.node_city
            reverse_path    += [city]

        return reverse_path[::-1]


    def get_children(self):
        missing_cities = self.get_missing_cities()

        if(len(self.cities) < len(missing_cities)):
            raise IndexError("Less Cities Than Visited Cities")

        return missing_cities


    def get_missing_cities(self):
        path         = self.get_path()
        cities_nodes = []

        for city in self.cities:
            if (city not in path):
                cities_nodes += [Node(self.cities, city, self.cost_table, self)]

        return cities_nodes


    def get_path_cost(self):
        tmp_node = self
        city     = self.node_city
        cost     = 0

        while(tmp_node.previous_node != None):
            city        = tmp_node.node_city
            tmp_node    = tmp_node.previous_node
            prev_city   = tmp_node.node_city

            cost += self.cost_table.loc[city, prev_city]

        return cost


    def get_mst(self, first_node, default=True):
        missing_cities  = self.get_missing_cities()
        if(default):
            missing_cities += [first_node]

        mst_costs = []

        for i in range(len(missing_cities)-1):
            for j in range(i+1, len(missing_cities)):
                node_a = missing_cities[i]
                node_b = missing_cities[j]

                city_a_name = node_a.node_city
                city_b_name = node_b.node_city

                mst_costs += [self.cost_table.loc[city_a_name, city_b_name]]

        mst_costs.sort()
        mst = mst_costs[:len(missing_cities)-1]
        return sum(mst)
