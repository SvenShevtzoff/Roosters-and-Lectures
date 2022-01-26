# =============================================================================
# simulatedannealing.py with random algorithm functions
# =============================================================================
from code.algorithms.randomise import randomise
from code.algorithms.hillclimber import mutate
import copy
import math
import random


TEMPERATURE_INTERVAL = 1/1000

def check_solution(new_schedule, current_schedule, no_change_count, temperature):
    # calculate the increase/decrease in fitness
    delta = new_schedule.fitness() - current_schedule.fitness()

    # calculate a probability of accepting the mutation
    if delta > 0:
        probability = math.exp(-delta / temperature)
    else:
        probability = 2

    # check if the mutation is accepted according to a random number
    if random.random() < probability:
        print(new_schedule.fitness())
        current_schedule = new_schedule
        no_change_count = 0
    else:
        # keep track of the amount of iterations without change
        no_change_count += 1

    # update temperature
    if temperature > 0.001:
        temperature -= TEMPERATURE_INTERVAL

    return no_change_count, temperature

def simulated_annealing(schedule, mutations=1):
    """The simulated annealing algorithm"""
    best_schedule = None
    iteration_counter_total = 0

    try:
        while True:
            # copy 'empty' schedule and fill it in by randomising a schedule
            copied_schedule = copy.deepcopy(schedule)
            current_schedule = randomise(copied_schedule)
            no_change_count = 0
            iteration_counter_total += 1
            iteration_counter_local = 0

            # reset temperature to 1
            temperature = 1

            while no_change_count < 1000:
                iteration_counter_local += 1
                print(iteration_counter_local)
                # copy the schedule
                new_schedule = copy.deepcopy(current_schedule)

                # make some mutations
                for _ in range(mutations):
                    mutate(new_schedule)

                # check if the mutation is accepted
                no_change_count, temperature = check_solution(new_schedule, current_schedule, no_change_count, temperature)

            # when iteration is done, save the schedule if it is the best schedule overall
            if best_schedule:
                if current_schedule.fitness() < best_schedule.fitness():
                    best_schedule = current_schedule
            else:
                best_schedule = current_schedule

    # ending the algorithm with a KeyboardInterrupt and finishing main.py
    except KeyboardInterrupt:
        return best_schedule