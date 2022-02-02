from code.algorithms.randomise import randomise
from code.algorithms.hillclimber import mutate, swap_activities, move_student


def improve_once(schedule, current_fitness):
    # make some mutations
    choice, mutation_parameters = mutate(schedule)

    # calculate the fitness after mutating
    new_fitness = schedule.fitness()

    # if the new schedule is better save it
    if new_fitness < current_fitness:
        # print(new_fitness)
        current_fitness = new_fitness
    else:
        # keep track of the amount of iterations without change
        if choice == 1:
            swap_activities(mutation_parameters[0], mutation_parameters[1])
        elif choice == 2:
            move_student(schedule, mutation_parameters[0].std_number(), mutation_parameters[2], mutation_parameters[1])


def baseline(schedule):
    schedule = randomise(schedule)
    while schedule.empty_roomslot_and_conflict_check()[0][3] > 0:
        fitness = schedule.fitness()
        improve_once(schedule, fitness)

    return schedule
