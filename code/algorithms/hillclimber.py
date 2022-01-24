# =============================================================================
# hillclimber.py with random algoritm functions
# =============================================================================

from code.algorithms.randomise import randomise
from helpers import swap_activities, move_students
import random

def hill_climber_alg(schedule, iterations, count_until_startover=100, mutations=5):
    oschedule = randomise(schedule)

    i = 0 
    while i != iterations:
        for _ in range(mutations):
            roomslot1 = random.choice(nschedule.roomslots().list())
            roomslot2 = random.choice(nschedule.roomslots().list())

            swap_activities(roomslot1, roomslot2)

        if nschedule.fitness() >= oschedule.fitness():
            nschedule = oschedule
            i += 1
        else:
            oschedule = nschedule
            i = 0
        
        print(nschedule.fitness())

    
        


    




    



# import copy
# import random

# from .randomise import randomise

# class HillClimber:

#     def __init__(self, schedule):
#         pass

#     def run():
#         pass
        # Kies een random start state
        # Herhaal:
        #     Doe een kleine random aanpassing
        #     Als de state is verslechterd:
        #         Maak de aanpassing ongedaan
