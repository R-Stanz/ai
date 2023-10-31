import random as rnd

class AStar:
    def __init__(self, cities, costs_table, mst_options):

        self.cities         = cities
        self.costs_table    = costs_table
        self.mst_options    = mst_options


    def run(self, is_first_operator=True):
        init_city = rnd.choice(cities)

        
    def mst(self, path):
        invalid_cities  = path.get_list()[1:]

        if (len(self.cities) < len(invalid_cities)):
            raise IndexError("Less Cities Than Visited Cities")
        
        i = 0
        count = 0
        mst_cost = 0
        while (count =! (len(self.cities) - len(invalid_cities)):

            if((self.mst_options[i][0] not in invalid_cities) and
               (self.mst_options[i][1] not in invalid_cities)):

               mst_cost += self.mst_options[i][2]
               count += 1

            i += 1
        return mst_cost
