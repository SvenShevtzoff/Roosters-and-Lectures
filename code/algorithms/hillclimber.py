# =============================================================================
# hillclimber.py with random algorithm functions
# =============================================================================
from code.algorithms.randomise import randomise
import copy
import random


def swap_activities(roomslot1, roomslot2):
    """Swaps the roomslots of two activities"""
    activity1 = roomslot1.activity()
    activity2 = roomslot2.activity()

    # swap activities
    if activity1 and activity2:
        helper = roomslot1
        activity1.set_roomslot(roomslot2)
        activity2.set_roomslot(helper)
    # move activity2 to empty roomslot
    elif not activity1 and activity2:
        activity2.set_roomslot(roomslot1)
        roomslot2.remove_activity()
    # move activity 1 to empty roomslot
    elif activity1 and not activity2:
        activity1.set_roomslot(roomslot2)
        roomslot1.remove_activity()


def move_student(schedule, student_key, from_activity_key, to_activity_key):
    """Moves a student from one activity (tutorial or practicum) to another"""
    # obtain the Activities and Student objects
    from_activity = schedule.activities().single(from_activity_key)
    to_activity = schedule.activities().single(to_activity_key)
    student = schedule.students().single(student_key)

    # removing and adding
    from_activity.remove_student(student_key)
    student.remove_activity(from_activity_key)
    to_activity.add_student(student_key)
    student.add_activity(to_activity_key)


def mutate(schedule):
    """This function chooses a mutation and then executes it"""
    all_activities = schedule.activities()
    all_roomslots = schedule.roomslots()
    all_students = schedule.students()
    mutation = random.choice([1, 2])

    if mutation == 1:
        # choose two random roomslots and swap their activities
        roomslot1 = random.choice(all_roomslots.list())
        roomslot2 = random.choice(all_roomslots.list())
        swap_activities(roomslot1, roomslot2)

        # the mutation kind and parameters are returned for undo
        return 1, [roomslot1, roomslot2]

    elif mutation == 2:
        # choose a random student from the schedule
        student = random.choice(all_students.list())
        # get all activities the student is enrolled in
        activities_keys = student.activities()
        # choose a random activity to move the student from
        from_activity_key = random.choice(activities_keys)

        # if the activity is not a lecture, find activities of the same course and kind
        # and swap student to a random one of these
        if all_activities.single(from_activity_key).kind() != "Lecture":
            activities_to_choose = []
            for activity_key in activities_keys:
                if all_activities.single(activity_key).course() == all_activities.single(from_activity_key).course():
                    if all_activities.single(activity_key).kind() == all_activities.single(from_activity_key).kind():
                        activities_to_choose.append(activity_key)
            to_activity_key = random.choice(activities_to_choose)

            # when the two activities are not the same move the student
            if from_activity_key != to_activity_key:
                move_student(schedule, student.std_number(), from_activity_key, to_activity_key)

                # the mutation kind and parameters are returned for undo
                return 2, [student, from_activity_key, to_activity_key]

        # dummy values are returned if no move is done
        return 3, []


def hill_climber_alg(schedule, iterations=100, no_change_count_max=1000):
    """The hill climber algorithm"""
    best_schedule = None
    best_schedule_fitness = None
    for _ in range(iterations):
        # copy 'empty' schedule and make a random state using randomise
        copied_schedule = copy.deepcopy(schedule)
        current_schedule = randomise(copied_schedule)
        current_fitness = current_schedule.fitness()
        no_change_count = 0

        while no_change_count < no_change_count_max:
            # make some mutations
            choice, mutation_parameters = mutate(current_schedule)

            # calculate the fitness after mutating
            new_fitness = current_schedule.fitness()

            # if the new schedule is better save it
            if new_fitness <= current_fitness:
                print(new_fitness)
                current_fitness = new_fitness
                no_change_count = 0
            else:
                # keep track of the amount of iterations without change
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
