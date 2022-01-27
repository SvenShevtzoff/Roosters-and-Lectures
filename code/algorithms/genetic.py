import imp
from code.algorithms.greedy import greedy
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy
import copy
import operator
import random

def genetic(schedule, population_size=10):

    scores = {}

    # make n start randomised schedules
    for _ in range(population_size):
        copied_schedule = copy.deepcopy(schedule)
        random_schedule = randomise(copied_schedule)
        scores[random_schedule] = random_schedule.fitness()

    # keep reproducing until all scores are the same
    while not all(score == list(scores.values())[0] for score in list(scores.values())):
        mean = sum(scores.values()) / len(scores)
        print(mean)

        mother = max(scores.items(), key=operator.itemgetter(1))[0]
        scores.pop(mother)

        father = max(scores.items(), key=operator.itemgetter(1))[0]

        fitness = mother.fitness()
        no_change_count = 0
        while (fitness >= (mother.fitness() and father.fitness())) and no_change_count < 100:
            no_change_count += 1
            child = copy.deepcopy(schedule)
            child.divide_students()
            for activity in child.activities().list():
                mothers_roomslot = mother.activities().dict()[str(activity)].roomslot()
                fathers_roomslot = father.activities().dict()[str(activity)].roomslot()
                roomslots_to_choose = [mothers_roomslot, fathers_roomslot]
                roomslot = random.choice(roomslots_to_choose)
                activity.set_roomslot(roomslot)
            fitness = child.fitness()

        scores[child] = child.fitness()
    
    return scores[list(scores.keys())[0]]








