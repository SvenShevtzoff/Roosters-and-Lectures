from code.algorithms.randomise import randomise
import copy
import operator
import random

def genetic(schedule, n=10):

    scores = {}

    for _ in range(n):
        copied_schedule = copy.deepcopy(schedule)
        random_schedule = randomise(copied_schedule)
        scores[random_schedule] = random_schedule.fitness()

    two_best_schedules = []

    mother = min(scores.items(), key=operator.itemgetter(1))[0]
    two_best_schedules.append(mother)

    scores.pop(mother)

    father = min(scores.items(), key=operator.itemgetter(1))[0]
    two_best_schedules.append(father)

    print(mother.fitness())
    print(father.fitness())

    child = copy.deepcopy(schedule)
    child.divide_students()

    for activity in child.activities().list():
        mothers_roomslot = mother.activities().dict()[str(activity)].roomslot()
        fathers_roomslot = father.activities().dict()[str(activity)].roomslot()
        roomslots_to_choose = [mothers_roomslot, fathers_roomslot]
        roomslot = random.choice(roomslots_to_choose)
        activity.set_roomslot(roomslot)
        print(child.fitness())






