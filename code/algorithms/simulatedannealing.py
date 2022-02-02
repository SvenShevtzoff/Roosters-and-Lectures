# =============================================================================
# simulatedannealing.py with random algorithm functions
# =============================================================================
from code.algorithms.randomise import randomise
from code.algorithms.hillclimber import mutate, swap_activities, move_student
import copy
import math
import random


TEMPERATURE_INTERVAL = 1/1000


def check_solution(new_fitness, current_fitness, temperature):
    """Accepts a solution based on a probability calculated by the temperature"""
    # calculate the increase/decrease in fitness
    delta = new_fitness - current_fitness

    # calculate a probability of accepting the mutation
    if temperature > TEMPERATURE_INTERVAL:
        if delta > 0:
            probability = math.exp(-delta / temperature)
        else:
            probability = 2
        temperature = update_temperature(temperature)
    else:
        if delta > 0:
            probability = 0
        else:
            probability = 2

    # check if the mutation is accepted according to a random number
    if random.random() < probability:
        return True, temperature
    else:
        # keep track of the amount of iterations without change
        return False, temperature


def update_temperature(temperature):
    "Updates the temperature after each iteration"
    temperature -= TEMPERATURE_INTERVAL

    return temperature


def simulated_annealing(schedule, iterations=100, no_change_count_max=1000):
    """The simulated annealing algorithm"""
    best_schedule = None
    best_schedule_fitness = None
    for _ in range(iterations):
        # copy 'empty' schedule and make a random state using randomise
        copied_schedule = copy.deepcopy(schedule)
        current_schedule = randomise(copied_schedule)
        current_fitness = current_schedule.fitness()
        no_change_count = 0
        temperature = 1

        while no_change_count < no_change_count_max:
            # make some mutations
            choice, mutation_parameters = mutate(current_schedule)

            # calculate the fitness after mutating
            new_fitness = current_schedule.fitness()
            boolean, temperature = check_solution(new_fitness, current_fitness, temperature)

            # new schedule accepted
            if boolean:
                current_fitness = new_fitness
                no_change_count = 0
            # new schedule rejected
            elif not boolean:
                if choice == 1:
                    swap_activities(mutation_parameters[0], mutation_parameters[1])
                elif choice == 2:
                    move_student(schedule, mutation_parameters[0].std_number(), mutation_parameters[2], mutation_parameters[1])
                no_change_count += 1

        # saving the best schedule
        if best_schedule:
            if current_fitness < best_schedule_fitness:
                best_schedule = current_schedule
                best_schedule_fitness = current_fitness
        else:
            best_schedule = current_schedule
            best_schedule_fitness = current_fitness
        no_change_count = 0
    return best_schedule
