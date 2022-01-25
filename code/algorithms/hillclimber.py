# =============================================================================
# hillclimber.py with random algorithm functions
# =============================================================================
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy
import copy
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


def move_student(schedule, student_key, from_activity_key, to_activity_key):
    """Moves a student from one activity to another"""
    schedule.activities().single(from_activity_key).remove_student(student_key)
    schedule.students.single(student_key).remove_activity(from_activity_key)
    schedule.activities().single(to_activity_key).add_student(student_key)
    schedule.students().single(student_key).add_activity(to_activity_key)

def mutate(schedule):
    all_activities = schedule.activities()
    all_roomslots = schedule.roomslots()
    mutation = random.choice([1, 2])

    if mutation == 1:
        roomslot1 = random.choice(all_roomslots.list())
        roomslot2 = random.choice(all_roomslots.list())
        swap_activities(roomslot1, roomslot2)
    elif mutation == 2:
        student = random.choice(schedule.students().list()) # student object
        activities = student.activities()
        from_activity_key = random.choice(activities) # string activity
        
        if all_activities.single(from_activity_key).kind() != "Lecture":
            activities_of_same_course = [activity for activity in activities if all_activities.single(activity).course() == all_activities.single(from_activity_key).course()]
            print(activities_of_same_course)
            activities_of_same_kind = [activity for activity in activities_of_same_course if all_activities.single(activity).kind() == all_activities.single(from_activity_key).kind()]
            print(activities_of_same_kind)
            to_activity_key = random.choice(activities_of_same_kind)

            if from_activity_key != to_activity_key:
                move_student(schedule, str(student), from_activity_key, to_activity_key)


def hill_climber_alg(schedule, mutations=5):
    no_change_count = 0
    best_schedule = None

    try:
        while True:
            copied_schedule = copy.deepcopy(schedule)
            current_schedule = randomise(copied_schedule)

            while no_change_count < 250:
                # copy the schedule
                new_schedule = copy.deepcopy(current_schedule)

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
                    best_schedule = copy.deepcopy(current_schedule)
            else:
                best_schedule = copy.deepcopy(current_schedule)
            no_change_count = 0

    except KeyboardInterrupt:
        return best_schedule
