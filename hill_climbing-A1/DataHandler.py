import matplotlib.pyplot as plt
from threading import Thread

class Data:

    def __init__(self):
        self.all_types_data = [[[] for j in range(3)] for i in range(8)]

    def add_data(self, stats, type):
        type -= 1
        data_by_type    = self.all_types_data[type]

        type_path_sizes, type_visited_totals, type_costs = data_by_type

        path_size, visited_total, cost = stats

        type_path_sizes     += [path_size]
        type_visited_totals += [visited_total]
        type_costs          += [cost]

    def plot(self, type_number):

        for type_number in range(len(self.all_types_data)):

            number_of_categories = len(self.all_types_data[type_number])
            fig, axs = plt.subplots(number_of_categories)

            fig.suptitle("General Infos About The Iterations")

            for category_number in range(number_of_categories):

                plot_index_a = type_number
                plot_index_b = category_number

                data_by_type            = self.all_types_data[type_number]
                data_by_type_category   = data_by_type[category_number]
                iterations_numbers      = [i for i in range(len(data_by_type_category))]

                axs[plot_index_a, plot_index_b].plot(iterations_numbers, data_by_type_category)

                category_name = self.get_category_name(category_number)
                msg = "Variation " + str(type_number+1) + ": " + category_name

                axs[plot_index_a, plot_index_b].set_title(msg)

            plt.show()

    def get_category_name(self, category_number):

                if(category_number == 0):
                    return "Path Size"
                elif(category_number == 1):
                    return "Total Of Visited States"
                elif(category_number == 2):
                    return "Final Cost"
                else:
                    raise IndexError("Getting More Than 3 Categoriesa.")
