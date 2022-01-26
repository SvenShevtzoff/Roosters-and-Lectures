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

    while len(scores) > 1:
        mean = sum(scores.values()) / len(scores)
        print(f"Number of schedules: {len(scores)}")
        print(f"Average malus points: {mean}")
        two_best_schedules = []

        mother = max(scores.items(), key=operator.itemgetter(1))[0]
        two_best_schedules.append(mother)

        scores.pop(mother)

        father = max(scores.items(), key=operator.itemgetter(1))[0]
        two_best_schedules.append(father)

        scores.pop(father)

        print(mother.fitness())
        print(father.fitness())

        fitness = max(mother.fitness(), father.fitness())
        while fitness >= (mother.fitness() and father.fitness()):
            child = copy.deepcopy(schedule)
            child.divide_students()
            for activity in child.activities().list():
                mothers_roomslot = mother.activities().dict()[str(activity)].roomslot()
                fathers_roomslot = father.activities().dict()[str(activity)].roomslot()
                roomslots_to_choose = [mothers_roomslot, fathers_roomslot]
                roomslot = random.choice(roomslots_to_choose)
                activity.set_roomslot(roomslot)
            fitness = child.fitness()

        print(child.fitness())

        scores[child] = child.fitness()
    
    print(scores)






