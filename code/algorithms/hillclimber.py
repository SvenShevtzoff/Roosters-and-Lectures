# =============================================================================
# hillclimber.py with random algorithm functions
# =============================================================================
from code.algorithms.greedy import greedy
from code.algorithms.randomise import randomise
import random

def swap_activities(roomslot1, roomslot2):
    activity1 = roomslot1.activity()
    activity2 = roomslot2.activity()
    if activity1 and activity2:
        helper = roomslot1
        activity1.set_roomslot(roomslot2)
        activity2.set_roomslot(helper)
    elif not activity1 and activity2:
        activity2.set_roomslot(roomslot1)
        roomslot2.remove_activity()
    elif activity1 and not activity2:
        activity1.set_roomslot(roomslot2)
        roomslot1.remove_activity()
    else:
        pass


def move_students(student, from_activity, to_activity):
    """Moves a student from one activity to another"""
    from_activity.remove_student(student)
    student.remove_activity(from_activity)
    to_activity.add_student(student)
    student.add_activity(to_activity)

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

        if current_schedule.fitness() > old_schedule.fitness():
            current_schedule = old_schedule
            i += 1
        else:
            old_schedule = current_schedule.copy()
            i = 0
        
        print(current_schedule.fitness(), i)
        

    
        

    



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
