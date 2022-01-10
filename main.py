from src.simulator import PopulationDensitySimulator
import keyboard

print('Welcome aboard!! We will do some population density simulation today')

number_of_people = int(input('Enter the total number of people (int only): '))

number_of_city = int(input('Enter the total number of cities you want to have (int only): '))

tau_value = float(input('Value of tau (0 represents people ar evenly distributed,'
                        ' 1 represents people live in big cities mostly: '))

object_of_class = PopulationDensitySimulator(total_population=number_of_people, number_of_cities=number_of_city, value_of_tau=tau_value)
object_of_class.run_initial_config()



counter = 0
while True:
    additional_population = input("Number of people you want to add to the population (enter 'e' to exit): ")
    if additional_population!='e':
        object_of_class.run_additional_population_step__(number_of_additional_population=int(additional_population),
                                                         number_of_times=counter)
        counter+=1
    else:
        break
