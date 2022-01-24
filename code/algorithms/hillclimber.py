# =============================================================================
# hillclimber.py with random algoritm functions
# =============================================================================

from code.helpers import swap_activities, move_students
from .randomise import randomise
import random


def mutate(schedule):
    roomslot1 = random.choice(schedule.roomslots().list())
    roomslot2 = random.choice(schedule.roomslots().list())

    swap_activities(roomslot1, roomslot2)

def hill_climber_alg(schedule, iterations):
    current_schedule = randomise(schedule)

    for iteration in range(iterations):
        # maak een kopie
        new_schedule = current_schedule.copy()

        # maak een mutatie
        mutate(new_schedule)

        # verbeterd
        print(f"{new_schedule.fitness()}, {current_schedule.fitness()}")
        if new_schedule.fitness() <= current_schedule.fitness():
            # print("if")
            current_schedule = new_schedule
        
    
    return current_schedule
