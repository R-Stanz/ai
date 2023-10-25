import pandas as pd
import random as rnd

class HillClimbing:

    def __init__(self, cities, costs_table, is_init_2=False):

        self.cities         = [i.name for i in cities]
        self.costs_table    = costs_table
        self.states_loaded  = 1

        sequel                  = self.cities
        if(is_init_2):
            self.current_state  = rnd.sample(sequel, len(sequel)) 

        else:
            self.current_state  = sequel

        self.current_cost       = self.sequel_cost(sequel)
        self.path               = [self.current_state]


    def sequel_cost(self, sequel):

        costs = [self.costs_table.loc[sequel[i], sequel[i+1]] 
                  for i in range(len(sequel)-1)]

        return sum(costs)


    def __str__(self):
        return f"Path: {self.path}\nStates Loaded: {self.states_loaded}\
                Current cost: {self.current_cost:.4E}"


    def hill_climb(self, is_first_oper=True):

        numb_of_cities = len(self.cities)

        a_city = -1
        while(a_city < numb_of_cities-3):
            a_city += 1
            b_city = a_city
            while(b_city < numb_of_cities-2):
                b_city += 1

                successor, cost = ["",0]
                if (is_first_oper):
                    successor, cost  = self.successor_1(a_city, b_city)
                else:
                    successor, cost = self.successor_2(a_city, b_city)

                self.states_loaded += 1

                if ((successor not in self.path) and 
                    (cost < self.current_cost)):

                    self.path           += [successor]
                    self.current_state   =  successor
                    self.current_cost    =  cost

                    a_city = -1
                    break

        return self

    def random_hill_climb(self, is_first_oper=True):

        numb_of_cities = len(self.cities)

        all_options =   [
                            (i, j)  for i in range(numb_of_cities-2)
                                    for j in range(i+1, numb_of_cities-1)
                        ]

        options = [i for i in all_options]

        while (len(options) > 0):

            a_index, b_index = options.pop(rnd.randrange(len(options)))

            if (is_first_oper):
                successor, cost  = self.successor_1(a_index, b_index)
            else:
                successor, cost = self.successor_2(a_index, b_index)

            self.states_loaded += 1

            if ((successor not in self.path) and 
                (cost < self.current_cost)):

                self.path           += [successor]
                self.current_state   =  successor
                self.current_cost    =  cost

                options = [i for i in all_options]

        return self

    def successor_1(self, a_index, b_index):

        successor = [i for i in self.current_state]

        a_city              = successor[a_index]
        successor[a_index]  = successor[b_index]
        successor[b_index]  = a_city

        return successor, self.sequel_cost(successor)


    def successor_2(self, a_index, b_index):

        successor = [i for i in self.current_state]

        section = successor[a_index:b_index+1]

        inverted_section = section[::-1]

        successor[a_index:b_index+1] = inverted_section[a_index:b_index+1]
        return successor, self.sequel_cost(successor)
