# =============================================================================
# hillclimber.py with random algorithm functions
# =============================================================================
from code.algorithms.randomise import randomise
from code.algorithms.greedy import greedy
import copy
import random

def swap_activities(roomslot1, roomslot2):
    """Swaps the roomslots of two activities"""
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


def move_student(schedule, student_key, from_activity_key, to_activity_key):
    """Moves a student from one activity (tutorial or practicum) to another"""
    # obtain the Activities and Student objects
    from_activity = schedule.activities().single(from_activity_key)
    to_activity = schedule.activities().single(to_activity_key)
    student = schedule.activities().single(student_key)

    # removing and adding
    from_activity.remove_student(student_key)
    student.remove_activity(from_activity_key)
    to_activity.add_student(student_key)
    student.add_activity(to_activity_key)


def mutate(schedule):
    """This function chooses a mutation and then executes it"""
    all_activities = schedule.activities()
    all_roomslots = schedule.roomslots()
    mutation = random.choice([1, 2])

    if mutation == 1:
        # choose two random roomslots and swap their activities
        roomslot1 = random.choice(all_roomslots.list())
        roomslot2 = random.choice(all_roomslots.list())
        swap_activities(roomslot1, roomslot2)
    elif mutation == 2:
        # choose a random student from the schedule
        student = random.choice(schedule.students().list())
        # these are all activities a student is enrolled in
        activities = student.activities()
        # choose a random activity to move the student from
        from_activity_key = random.choice(activities)
        
        # if the activity is not a lecture, find activities of the same course and kind and swap student to a random one of these
        if all_activities.single(from_activity_key).kind() != "Lecture":
            activities_of_same_course = [activity for activity in activities if all_activities.single(activity).course() == all_activities.single(from_activity_key).course()]
            activities_of_same_kind = [activity for activity in activities_of_same_course if all_activities.single(activity).kind() == all_activities.single(from_activity_key).kind()]
            to_activity_key = random.choice(activities_of_same_kind)

            if from_activity_key != to_activity_key:
                move_student(schedule, str(student), from_activity_key, to_activity_key)


def hill_climber_alg(schedule, mutations=5):
    """The hill climber algorithm"""
    no_change_count = 0
    best_schedule = None

    try:
        while True:
            # copy 'empty' schedule and fill it in by randomising a schedule
            copied_schedule = copy.deepcopy(schedule)
            current_schedule = randomise(copied_schedule)

            while no_change_count < 250:
                # copy the schedule
                new_schedule = copy.deepcopy(current_schedule)

                # make some mutations
                for _ in range(mutations):
                    mutate(new_schedule)

                # if the new schedule is better save it
                if new_schedule.fitness() < current_schedule.fitness():
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
