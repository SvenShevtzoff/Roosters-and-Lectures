from code.algorithms.randomise import randomise
from code.classes.roomslots import Roomslot
import copy
import operator
import random
from collections import Counter

def genetic(schedule, population_size=10):

    scores = {}
    hundred_in_a_row = 0

    for _ in range(population_size):
        copied_schedule = copy.deepcopy(schedule)
        random_schedule = randomise(copied_schedule)
        scores[random_schedule] = random_schedule.fitness()

    while not all(score == list(scores.values())[0] for score in list(scores.values())):
        mother = max(scores.items(), key=operator.itemgetter(1))[0]
        scores.pop(mother)
        father = max(scores.items(), key=operator.itemgetter(1))[0]

        fitness = mother.fitness()
        wrong_times = 0

        while fitness >= father.fitness() and wrong_times < 100:
            available_roomslots = []
            roomslots_used = []
            for slot in schedule.roomslots().list():
                available_roomslots.append(str(slot))

            wrong_times += 1
            print(wrong_times)
            child = copy.deepcopy(schedule)
            child.divide_students()

            for activity in child.activities().list():
                mothers_roomslot = mother.activities().dict()[str(activity)].roomslot()
                fathers_roomslot = father.activities().dict()[str(activity)].roomslot()

                roomslot = random.choice([mothers_roomslot, fathers_roomslot])

                if str(roomslot) in available_roomslots:
                    activity.set_roomslot(roomslot)
                    available_roomslots.remove(str(roomslot))
                    roomslots_used.append(str(roomslot))
                else:
                    if str(roomslot) == str(mothers_roomslot):
                        roomslot = fathers_roomslot
                        if str(roomslot) in available_roomslots:
                            activity.set_roomslot(roomslot)
                            available_roomslots.remove(str(roomslot))
                            roomslots_used.append(str(roomslot))
                    else:
                        roomslot = mothers_roomslot
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
            
            fitness = child.fitness()

        if wrong_times == 100:
            hundred_in_a_row += 1

        if hundred_in_a_row == 4:
            scores.pop(child)
        print(f"Malus points of child: {child.fitness()}")
        scores[child] = child.fitness()
        if hundred_in_a_row == 4:
            scores.pop(child)
        print(list(scores.values()))



