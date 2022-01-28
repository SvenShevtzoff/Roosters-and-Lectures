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
<<<<<<< HEAD
=======
        print(mean)
>>>>>>> c8ede900967eea3e737a5604d365b8a66ba9c2e0

        mother = max(scores.items(), key=operator.itemgetter(1))[0]
        scores.pop(mother)

        for activity in mother.activities().list():
            print(f"Activity: {activity} roomslot: {activity.roomslot()}")

        father = max(scores.items(), key=operator.itemgetter(1))[0]

<<<<<<< HEAD
        print("Father schedule")
        for activity in father.activities().list():
            print(f"Activity: {activity} roomslot: {activity.roomslot()}")

        # print(mother.fitness())
        # print(father.fitness())

        fitness = max(mother.fitness(), father.fitness())
        wrong_times = 0
        while (fitness >= (mother.fitness() and father.fitness())) and wrong_times < 100:
            available_mother = []
            available_father = []
            for roomslot in schedule.roomslots().list():
                available_mother.append(str(roomslot))
                available_father.append(str(roomslot))
            wrong_times += 1
            print(wrong_times)
=======
        fitness = mother.fitness()
        no_change_count = 0
        while (fitness >= (mother.fitness() and father.fitness())) and no_change_count < 100:
            no_change_count += 1
>>>>>>> c8ede900967eea3e737a5604d365b8a66ba9c2e0
            child = copy.deepcopy(schedule)
            child.divide_students()
            random_child_schedule = randomise(child)
            for activity in child.activities().list():
                print(str(activity))
                mothers_roomslot = mother.activities().dict()[str(activity)].roomslot()
                print(f"Mothers roomslot: {str(mothers_roomslot)}")
                fathers_roomslot = father.activities().dict()[str(activity)].roomslot()
                print(f"Fathers roomslot: {str(fathers_roomslot)}")
                roomslots_to_choose = [mothers_roomslot, fathers_roomslot]
                roomslot = random.choice(roomslots_to_choose)
<<<<<<< HEAD
                if str(roomslot) == str(mothers_roomslot):
                    print("Chose mothers roomslot")
                    if str(roomslot) in available_mother:
                        print("Roomslot was not taken from father yet")
                        print()
                        activity.set_roomslot(roomslot)
                        available_father.remove(str(roomslot))
                    else:
                        activity.set_roomslot(fathers_roomslot)
                elif str(roomslot) == str(fathers_roomslot):
                    print("Chose fathers roomslot")
                    if str(roomslot) in available_father:
                        print("Roomslot was not taken from mother yet")
                        print()
                        activity.set_roomslot(roomslot)
                        available_mother.remove(str(roomslot))
                    else:
                        activity.set_roomslot(mothers_roomslot)
                    
            fitness = random_child_schedule.fitness()
        
        print(random_child_schedule.fitness())

        scores[random_child_schedule] = random_child_schedule.fitness()
    
        # if every score is the same, spice it up with some mutations
        # for key in list(scores.keys())[0:2]:
        #     scores.pop(key)
        #     another_copied_schedule = copy.deepcopy(schedule)
        #     mutation = randomise(another_copied_schedule)
        #     scores[mutation] = mutation.fitness()
=======
                activity.set_roomslot(roomslot)
            fitness = child.fitness()

        scores[child] = child.fitness()
>>>>>>> c8ede900967eea3e737a5604d365b8a66ba9c2e0
    
    return scores[list(scores.keys())[0]]








