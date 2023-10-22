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

        for i in range(numb_of_cities):
            for j in range(i+1, numb_of_cities):

                successor, cost = ["",0]
                if (is_first_oper):
                    successor, cost  = self.successor_1(i, j)
                else:
                    successor, cost = self.successor_2(i, j)

                self.states_loaded += 1

                if ((successor not in self.path) and 
                    (cost < self.current_cost)):

                    self.path           += [successor]
                    self.current_state   =  successor
                    self.current_cost    =  cost
                    i = 0
                    j = 1

        return self


    def successor_1(self, a_index, b_index):

        successor = [i for i in self.current_state]

        a_city              = successor[a_index]
        successor[a_index]  = successor[b_index]
        successor[b_index]  = a_city

        cost = self.sequel_cost(successor)

        return successor, cost


    def successor_2(i, j):
        pass
