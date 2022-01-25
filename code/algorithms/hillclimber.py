# =============================================================================
# hillclimber.py with random algorithm functions
# =============================================================================
from code.algorithms.greedy import greedy
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy
from code.classes.schedule import Schedule
from code.load import load
import random
import time

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

def hill_climber_alg(schedule, mutations=5):
    no_change_count = 0
    best_schedule = None

    try:
        while True:
            copied_schedule = schedule.copy()
            current_schedule = randomise(copied_schedule)

            while no_change_count < 250:
                # copy the schedule
                new_schedule = current_schedule.copy()

                # make some mutations
                for _ in range(mutations):
                    mutate(new_schedule)

                # if the new schedule is better save it
                if new_schedule.fitness() <= current_schedule.fitness():
                    print(new_schedule.fitness())
                    current_schedule = new_schedule
                    no_change_count = 0
                else:
                    # keep track of the amount of iterations without change
                    no_change_count += 1

            if best_schedule:
                if current_schedule.fitness() < best_schedule.fitness():
                    best_schedule = current_schedule.copy()
            else:
                best_schedule = current_schedule.copy()
            no_change_count = 0

    except KeyboardInterrupt:
        return current_schedule
