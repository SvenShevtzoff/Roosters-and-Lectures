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

    



