
from code.algorithms.randomise import randomise
from code.algorithms.hillclimber import mutate, swap_activities, move_student


def improve_once(schedule, current_fitness):
    # make a mutation
    choice, mutation_parameters = mutate(schedule)

    # calculate the fitness after mutating
    new_fitness = schedule.fitness()

    # if the new schedule is better save it
    if new_fitness < current_fitness:
        current_fitness = new_fitness
    else:
        # if not, make another mutation
        if choice == 1:
            swap_activities(mutation_parameters[0], mutation_parameters[1])
        elif choice == 2:
            move_student(schedule, mutation_parameters[0].std_number(), mutation_parameters[2], mutation_parameters[1])


def randomise_baseline(schedule):
    """Create a random schedule and change it using a hillclimber until it is valid"""
    schedule = randomise(schedule)

    # keep improving by one step until there are no students with three gap hours, which makes the schedule valid
    while schedule.empty_roomslot_and_conflict_check()[0][3] > 0:
        fitness = schedule.fitness()
        improve_once(schedule, fitness)

    return schedule

