import numpy as np
import matplotlib.pyplot as plt

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

    def basic_plot(self):

        for type_number in range(len(self.all_types_data)):

            number_of_categories = len(self.all_types_data[type_number])
            for category_number in range(number_of_categories):

                fig, ax = plt.subplots()

                fig.suptitle("General Infos About The Iterations")

                data_by_type            = self.all_types_data[type_number]
                data_by_type_category   = data_by_type[category_number]
                iterations_numbers      = [i for i in range(len(data_by_type_category))]

                proportions, labels = self.get_proportions(data_by_type_category)
                ax.pie(proportions, labels=labels, autopct='%1.4f%%',
                       pctdistance=1.25, labeldistance=.6)

                category_name = self.get_category_name(category_number)
                msg = "Variation " + str(type_number+1) + ": " + category_name

                ax.set_title(msg)

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


    def get_proportions(self, data):
        proportions = []
        labels      = []

        for i in data:
            i_formated = '%.2f'%(i)
            if (i_formated not in labels):
                labels      += [i_formated]
                proportions += [data.count(i)/len(data)]

        return proportions, labels

    def get_avg_path_size(self):

        msg = "\n"

        i = 0
        avg_arr = []
        for variation in self.all_types_data:
            i += 1
            variation_avg = np.mean(variation[0])
            avg_arr += [variation_avg] 
            msg += "\nVariation " + str(i) + " Average Path Size: " + '%.4f'%(variation_avg)

        msg += "\n\n\t=>Overall Path Size Average: " + '%.4f'%(np.mean(avg_arr))
        return msg


    def get_avg_loaded(self):

        msg = "\n"

        i = 0
        avg_arr = []
        for variation in self.all_types_data:
            i += 1
            variation_avg = np.mean(variation[1])
            avg_arr += [variation_avg] 
            msg += "\nVariation " + str(i) + " Average Number Of Visited Configurations: " + '%.4f'%(variation_avg)

        msg += "\n\n\t=>Overall Average Number Of Visited Configurations Average: " + '%.4f'%(np.mean(avg_arr))
        return msg


    def get_avg_final_cost(self):

        msg = "\n"

        i = 0
        avg_arr = []
        for variation in self.all_types_data:
            i += 1
            variation_avg = np.mean(variation[2])
            avg_arr += [variation_avg] 
            msg += "\nVariation " + str(i) + " Average Final Cost: " + '%.4f'%(variation_avg)

        msg += "\n\n\t=>Overall Average Final Cost: " + '%.4f'%(np.mean(avg_arr))
        return msg
