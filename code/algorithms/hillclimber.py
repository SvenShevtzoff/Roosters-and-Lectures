# =============================================================================
# hillclimber.py with random algorithm functions
# =============================================================================

from code.algorithms.randomise import randomise
from code.algorithms.helpers import swap_activities, move_students
import random

def hill_climber_alg(schedule, iterations, count_until_startover=100, mutations=1):
    current_schedule = randomise(schedule)
    old_schedule = current_schedule.copy()
    i = 0 
    while i != count_until_startover:

        #     Doe een kleine random aanpassing
        for _ in range(mutations):
            roomslot1 = random.choice(current_schedule.roomslots().list())
            roomslot2 = random.choice(current_schedule.roomslots().list())

            swap_activities(roomslot1, roomslot2)

        if current_schedule.fitness() > old_schedule.fitness():
            current_schedule = old_schedule
            print("v")
            i += 1
        else:
            old_schedule = current_schedule.copy()
            print("b")
            i = 0

    
        


    



# <<<<<<< HEAD

    



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
        
       
        #         Maak de aanpassing ongedaan
#         swap_activities(roomslot1, roomslot2)
