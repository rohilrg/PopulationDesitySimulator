import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class PopulationDensitySimulator:

    def __init__(self, number_of_cities, total_population, value_of_tau=0.5):
        self.number_of_cites = number_of_cities
        self.total_population = total_population
        self.value_of_tau = value_of_tau
        self.__ratio__of_big_city_population__ = []
        self.__ratio__of_small_city_population__ = []
    def __get_number_of_people_per_city__(self):

        number_of_big_cites, \
        number_of_people_living_in_big_cites,\
        number_of_people_living_in_small_cites, \
        number_of_small_cites = self.__get_the_big_and_small_city_distribution__(self.total_population)

        #######################################################################

        # dataframe containing the number of people and the city number

        ## let's start empty dataframe

        dataframe_number_of_people_distribution = pd.DataFrame()

        ## fill it with big city numbers
        if number_of_big_cites != 0:
            list_of_big_cities_and_their_population, ratios_of_big_cities_and_their_population\
                = self.__get_list_of_cites_population__(number_of_people_living_in_big_cites,
                number_of_big_cites)
            self.__ratio__of_big_city_population__ = ratios_of_big_cities_and_their_population
        else:
            list_of_big_cities_and_their_population = []
            self.__ratio__of_big_city_population__ = []
        ## fill it with small city numbers
        if number_of_small_cites!=0:
            list_of_small_cities_and_their_population, \
            ratios_of_small_cities_and_their_population= self.__get_list_of_cites_population__(
                number_of_people_living_in_small_cites, number_of_small_cites)
            self.__ratio__of_small_city_population__ = ratios_of_small_cities_and_their_population
        else:
            list_of_small_cities_and_their_population = []
            self.__ratio__of_small_city_population__ = []

        ## fill the database now
        counter = 0
        for idx, i in enumerate(list_of_big_cities_and_their_population):
            dataframe_number_of_people_distribution.loc[counter, 'city_number'] = counter+1
            dataframe_number_of_people_distribution.loc[counter, 'population'] = i
            dataframe_number_of_people_distribution.loc[counter, 'radius_of_circle']\
                = 20*math.sqrt((i*self.number_of_cites)/(self.total_population*3.14))
            counter+=1

        for idx, i in enumerate(list_of_small_cities_and_their_population):
            dataframe_number_of_people_distribution.loc[counter, 'city_number'] = counter+1
            dataframe_number_of_people_distribution.loc[counter, 'population'] = i
            dataframe_number_of_people_distribution.loc[counter, 'radius_of_circle'] \
                = 20*math.sqrt((i * self.number_of_cites) / (self.total_population * 3.14))
            counter+=1
        self.initial_dataframe = dataframe_number_of_people_distribution
        self.initial_dataframe.to_csv(
            f'output/dataframe/initial_df_with_{str(self.total_population)}_{self.number_of_cites}_{self.value_of_tau}.csv',
            index=False)
        return dataframe_number_of_people_distribution

    def __get_the_big_and_small_city_distribution__(self, total_population):
        # number of big cites are given by the following equation
        ratio_of_big_cites = 0.3283081 * math.exp((-(self.value_of_tau - 0.5552639) ** 2 / (2 * 0.2253474 ** 2)))
        number_of_big_cites = int(ratio_of_big_cites * self.number_of_cites)
        if number_of_big_cites == 0:
            number_of_big_cites = number_of_big_cites + 1
        ## number of small cites
        number_of_small_cites = self.number_of_cites - number_of_big_cites
        ######################################################################
        ## number of people living in big cites
        ratio_of_people_living_in_big_cites = 0.96338271 * math.exp(
            -(self.value_of_tau - 0.9441574) ** 2 / (2 * 0.4118766 ** 2))
        number_of_people_living_in_big_cites = int(total_population * ratio_of_people_living_in_big_cites)
        ### number of people in small cites
        number_of_people_living_in_small_cites = total_population - number_of_people_living_in_big_cites
        return number_of_big_cites, number_of_people_living_in_big_cites, number_of_people_living_in_small_cites, number_of_small_cites

    def __get_list_of_cites_population__(self, number_of_people_living_in_cites, number_of_cites):
        random_numbers = random.sample(range(1, 300), number_of_cites)
        list_of_cities_and_their_population = \
            [int(i / sum(random_numbers) * number_of_people_living_in_cites) for i in random_numbers]
        ratios_of_cities_and_their_population = [i / sum(random_numbers) for i in random_numbers]
        # if sum of people living in cites is not equal to number_of_people_living_in_cites
        # than add to random city
        if number_of_people_living_in_cites != sum(list_of_cities_and_their_population):
            list_of_cities_and_their_population[-1] = list_of_cities_and_their_population[-1] + \
                                                          (number_of_people_living_in_cites
                                                           - sum(list_of_cities_and_their_population))
        return list_of_cities_and_their_population, ratios_of_cities_and_their_population

    def __add_additonal_poulation__(self, number_of_additional_population, number_of_times):

        number_of_big_cites,\
        number_of_people_living_in_big_cites,\
        number_of_people_living_in_small_cites, number_of_small_cites =\
            self.__get_the_big_and_small_city_distribution__(number_of_additional_population)

        ######################################################################

        ## fill it with big city numbers
        if number_of_big_cites != 0:
            list_of_big_cities_and_their_population = \
                [int(i * number_of_people_living_in_big_cites) for i in self.__ratio__of_big_city_population__]
            # if sum of people living in big cites is not equal to number_of_people_living_in_big_cites
            # than add to random city
            if number_of_people_living_in_big_cites != sum(list_of_big_cities_and_their_population):
                list_of_big_cities_and_their_population[-1] = list_of_big_cities_and_their_population[-1] + \
                                                          (number_of_people_living_in_big_cites
                                                           - sum(list_of_big_cities_and_their_population))
        else:
            list_of_big_cities_and_their_population = []
        ## fill it with small city numbers
        if number_of_small_cites != 0:
            list_of_small_cities_and_their_population = \
                [int(i * number_of_people_living_in_small_cites) for i in self.__ratio__of_small_city_population__]
            # if sum of people living in small cites is not equal to number_of_people_living_in_small_cites
            # than add to random city
            if number_of_people_living_in_small_cites != sum(list_of_small_cities_and_their_population):
                list_of_small_cities_and_their_population[-1] = list_of_small_cities_and_their_population[-1] + \
                                                              (number_of_people_living_in_big_cites
                                                               - sum(list_of_small_cities_and_their_population))
        else:
            list_of_small_cities_and_their_population = []

        ## fill the database now
        counter = 0
        dataframe_number_of_people_distribution = pd.DataFrame()
        for idx, i in enumerate(list_of_big_cities_and_their_population):
            dataframe_number_of_people_distribution.loc[counter, 'city_number'] = counter + 1
            dataframe_number_of_people_distribution.loc[counter, f'population_additional_{number_of_times}'] = i
            dataframe_number_of_people_distribution.loc[counter, f'radius_of_circle_additional_{number_of_times}'] \
                = 20*math.sqrt((i * self.number_of_cites) / (self.total_population * 3.14))
            counter += 1

        for idx, i in enumerate(list_of_small_cities_and_their_population):
            dataframe_number_of_people_distribution.loc[counter, 'city_number'] = counter + 1
            dataframe_number_of_people_distribution.loc[counter, f'population_additional_{number_of_times}'] = i
            dataframe_number_of_people_distribution.loc[counter, f'radius_of_circle_additional_{number_of_times}'] \
                = 20*math.sqrt((i * self.number_of_cites) / (self.total_population * 3.14))
            counter += 1
        return dataframe_number_of_people_distribution

    def __return_random_points_on_cartisian_plot__(self):
        ## randomly select m cities on cartisian plot

        self.array_for_random_points = np.stack(
            [np.random.choice(range(1000), 2, replace=False) for _ in range(self.number_of_cites)])


    def __draw_the_cities_and_circle__(self, dataframe_with_population_and_radius, column_for_radius= 'radius_of_circle'):
        fig, ax = plt.subplots()
        # plt.rc('text', usetex=True)
        # plt.rc('font', family='serif')
        plt.plot(self.array_for_random_points[:,0], self.array_for_random_points[:,1],
                 marker='.', color='k', linestyle='None')
        plt.xlim(0,999)
        plt.ylim(0,999)
        plt.title(f'Population density')
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        for idx, row in dataframe_with_population_and_radius.iterrows():
            point_array = list(self.array_for_random_points[idx])

            circle1 = plt.Circle((point_array[0], point_array[1]), row[column_for_radius], color='r', fill=False)
            ax.add_artist(circle1)
        plt.show()

    def run_initial_config(self):

        self.__get_number_of_people_per_city__()
        self.__return_random_points_on_cartisian_plot__()
        self.__draw_the_cities_and_circle__(self.initial_dataframe, column_for_radius= 'radius_of_circle')

    def run_additional_population_step__(self, number_of_additional_population, number_of_times=1):

        additional_dataframe = self.__add_additonal_poulation__(number_of_additional_population, number_of_times)

        combined_df = self.initial_dataframe.merge(additional_dataframe, on=['city_number'])

        combined_df[f'radius_of_circle_new_{number_of_times}'] = combined_df['radius_of_circle'] + combined_df[f'radius_of_circle_additional_{number_of_times}']

        self.__draw_the_cities_and_circle__(combined_df, column_for_radius=f'radius_of_circle_new_{number_of_times}')

        self.initial_dataframe = combined_df
        # save the dataframes

        combined_df.to_csv(f'output/dataframe/'
                           f'additional_population_df_with_{str(self.total_population)}_'
                           f'{self.number_of_cites}_{self.value_of_tau}_{number_of_additional_population}_number_of_times_{str(number_of_times)}.csv', index=False)

if __name__ == '__main__':

    et=PopulationDensitySimulator(number_of_cities=10, total_population=1000000, value_of_tau=0.75)

    et.run_initial_config()

    et.run_additional_population_step__(number_of_additional_population=1000000)



