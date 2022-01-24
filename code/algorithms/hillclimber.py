# =============================================================================
# hillclimber.py with random algoritm functions
# =============================================================================

from helpers import swap_activities, move_students
import random

def hill_climber_alg(schedule):
    copied_schedule = 

    for _ in range(100):
        roomslot1 = random.choice(schedule.roomslots().list())
        roomslot2 = random.choice(schedule.roomslots().list())

        swap_activities(roomslot1, roomslot2)

    



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
