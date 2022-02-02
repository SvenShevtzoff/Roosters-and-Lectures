from code.algorithms.randomise import randomise
from code.algorithms.hillclimber import swap_activities, move_student
from collections import Counter
import copy
import operator
import random


def make_childeren(parent1, parent2, child, schedule):
    available_roomslots = []
    roomslots_used = []
    for slot in schedule.roomslots().list():
        available_roomslots.append(str(slot))

    for activity in child.activities().list():
        genome1 = parent1.activities().dict()[str(activity)].roomslot()
        genome2 = parent2.activities().dict()[str(activity)].roomslot()

        roomslot = random.choice([genome1, genome2])

        if str(roomslot) in available_roomslots:
            activity.set_roomslot(roomslot)
            available_roomslots.remove(str(roomslot))
            roomslots_used.append(str(roomslot))
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

    for activity in child.activities().list():
        if not activity.roomslot():
            roomslot_key = random.choice(available_roomslots)
            roomslot = schedule.roomslots().single(roomslot_key)
            activity.set_roomslot(roomslot)
            available_roomslots.remove(str(roomslot))
            roomslots_used.append(str(roomslot))

    return child


def mutations(child):
    mutation = random.choice([1, 2])

    if mutation == 1:
        all_activities = child.activities()
        swap = random.sample(all_activities.list(), 2)
        swap = [_.roomslot() for _ in swap]
        swap_activities(swap[0], swap[1])

    elif mutation == 3:
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


def genetic(schedule, number_of_childeren=10, number_of_bests=5, i=1000):
    parents = [randomise(copy.deepcopy(schedule)) for _ in range(number_of_childeren)]

    for i in range(i):
        parents = {parent: parent.fitness() for parent in parents}
        parents = list(dict(sorted(parents.items(), key=operator.itemgetter(1), reverse=False)[:number_of_bests]))
        number_of_mutations = Counter([p.fitness() for p in parents])
        number_of_mutations = max(number_of_mutations.values())
        childs = []

        for _ in range(number_of_childeren):
            child = copy.deepcopy(schedule)
            child.divide_students()

            parents_choice = random.sample(parents, 2)
            child = make_childeren(parents_choice[0], parents_choice[1], child, schedule)

            for _ in range(number_of_mutations):
                child = mutations(child)

            childs.append(child)

        parents = copy.deepcopy(childs)

    child = {parent: parent.fitness() for parent in parents}
    best_child = list(dict(sorted(child.items(), key=operator.itemgetter(1), reverse=False)[:1]))[0]
    return best_child
