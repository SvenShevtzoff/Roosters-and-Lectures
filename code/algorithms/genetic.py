from code.algorithms.randomise import randomise
import copy
import operator
import random

def genetic(schedule, n=10):

    scores = {}

    # make n start randomised schedules
    for _ in range(n):
        copied_schedule = copy.deepcopy(schedule)
        random_schedule = randomise(copied_schedule)
        scores[random_schedule] = random_schedule.fitness()

    # keep reproducing until all scores are the same
    while not all(score == list(scores.values())[0] for score in list(scores.values())):
        print(list(scores.values()))
        mean = sum(scores.values()) / len(scores)
        print(f"Average malus points: {mean}")

        mother = max(scores.items(), key=operator.itemgetter(1))[0]
        scores.pop(mother)

        father = max(scores.items(), key=operator.itemgetter(1))[0]

        print(mother.fitness())
        print(father.fitness())

        fitness = max(mother.fitness(), father.fitness())
        wrong_times = 0
        while (fitness >= (mother.fitness() and father.fitness())) and wrong_times < 100:
            wrong_times += 1
            print(wrong_times)
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
    
        # if every score is the same, spice it up with some mutations
        # for key in list(scores.keys())[0:2]:
        #     scores.pop(key)
        #     another_copied_schedule = copy.deepcopy(schedule)
        #     mutation = randomise(another_copied_schedule)
        #     scores[mutation] = mutation.fitness()
    
    return scores[list(scores.keys())[0]]








