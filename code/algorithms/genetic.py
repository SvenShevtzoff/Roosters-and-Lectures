# =============================================================================
# generic.py with generic algoritm functions
# =============================================================================
from code.algorithms.randomise import randomise
from code.algorithms.hillclimber import swap_activities, move_student
from collections import Counter
import copy
import operator
import random


def make_childeren(parent1, parent2, child, schedule):
    """Function makes a child of two parents"""
    available_roomslots = []
    roomslots_used = []

    # making a list with available roomslots
    for slot in schedule.roomslots().list():
        available_roomslots.append(str(slot))

    # take from both parents the roomslot an activity
    for activity in child.activities().list():
        genome1 = parent1.activities().dict()[str(activity)].roomslot()
        genome2 = parent2.activities().dict()[str(activity)].roomslot()

        # randomly deciding which roomslot to give to the child
        roomslot = random.choice([genome1, genome2])

        # if chosen roomslot in available give the it to the child
        if str(roomslot) in available_roomslots:
            activity.set_roomslot(roomslot)
            available_roomslots.remove(str(roomslot))
            roomslots_used.append(str(roomslot))
        # if chosen roomslot unavailable try roomslot of other parent
        else:
            if str(roomslot) == str(genome1):
                roomslot = genome2
                if str(roomslot) in available_roomslots:
                    activity.set_roomslot(roomslot)
                    available_roomslots.remove(str(roomslot))
                    roomslots_used.append(str(roomslot))
            else:
                roomslot = genome1
                if str(roomslot) in available_roomslots:
                    activity.set_roomslot(roomslot)
                    available_roomslots.remove(str(roomslot))
                    roomslots_used.append(str(roomslot))

    # when there are still activities without a roomslot in the end, give them a random roomslot
    for activity in child.activities().list():
        if not activity.roomslot():
            roomslot_key = random.choice(available_roomslots)
            roomslot = schedule.roomslots().single(roomslot_key)
            activity.set_roomslot(roomslot)
            available_roomslots.remove(str(roomslot))
            roomslots_used.append(str(roomslot))

    return child


def mutations(child):
    """Mutates child in the same way as in hillclimber function"""
    # take random one of the two availible mutations
    mutation = random.choice([1, 2])

    # swap activities to other roomslot
    if mutation == 1:
        all_activities = child.activities()
        swap = random.sample(all_activities.list(), 2)
        swap = [_.roomslot() for _ in swap]
        swap_activities(swap[0], swap[1])

    # move a student to another group
    elif mutation == 2:
        all_activities = child.activities()
        all_students = child.students()
        student = random.choice(all_students.list())
        activities_keys = student.activities()
        from_activity_key = random.choice(activities_keys)

        if all_activities.single(from_activity_key).kind() != "Lecture":
            activities_to_choose = []
            for activity_key in activities_keys:
                if all_activities.single(activity_key).course() == all_activities.single(from_activity_key).course():
                    if all_activities.single(activity_key).kind() == all_activities.single(from_activity_key).kind():
                        activities_to_choose.append(activity_key)
            to_activity_key = random.choice(activities_to_choose)

            if from_activity_key != to_activity_key:
                move_student(child, student.std_number(), from_activity_key, to_activity_key)

    return child


def genetic(schedule, number_of_childeren=10, number_of_bests=5, iterations=1000):
    """Function for genetic algorithm"""
    # create a population of random parents
    parents = [randomise(copy.deepcopy(schedule)) for _ in range(number_of_childeren)]

    for i in range(iterations):
        # take the best children of the population
        parents = {parent: parent.fitness() for parent in parents}
        parents = list(dict(sorted(parents.items(), key=operator.itemgetter(1), reverse=False)[:number_of_bests]))
        # decide how many mutations every child gets
        number_of_mutations = Counter([p.fitness() for p in parents])
        number_of_mutations = max(number_of_mutations.values())
        childs = []

        for _ in range(number_of_childeren):
            # make an empty child
            child = copy.deepcopy(schedule)
            child.divide_students()

            # take two different parents form the parents population
            parents_choice = random.sample(parents, 2)

            # make a child form those parents
            child = make_childeren(parents_choice[0], parents_choice[1], child, schedule)

            # give the child a number of mutations
            for _ in range(number_of_mutations):
                child = mutations(child)

            childs.append(child)

        # the children become the new parents
        parents = copy.deepcopy(childs)

    # take the best child from the last generation
    child = {parent: parent.fitness() for parent in parents}
    best_child = list(dict(sorted(child.items(), key=operator.itemgetter(1), reverse=False)[:1]))[0]

    return best_child
