import pandas as pd
from IPython.display import display


def dict_to_df(roomslots):
    df = pd.DataFrame(columns=["day", "time", "room", "activity"])
    for slot in roomslots.get_list():
        if not slot.get_activity():
            df = df.append({
                "day": slot.get_day(),
                "time": slot.get_time(),
                "room": slot.get_room(),
                "activity": None,
                "students": None}, 
                ignore_index=True)
        else:
            students = []
            for student in slot.get_course().get_students():
                students.append(student)
            df = df.append({
                "day": slot.get_day(),
                "time": slot.get_time(),
                "room": slot.get_room(),
                "activity": slot.get_activity(),
                "students": students}, 
                ignore_index=True)
    return df



def fitness_function(schedule_to_check):
    schedule = dict_to_df(schedule_to_check)

    malus_points = 0

    # aantal studenten groter dan maximum toegestaan in de zaal (1)
    for i in schedule.index:
        if schedule["activity"][i]:
            number_of_students = len(schedule["students"][i])
            room_capacity = schedule["room"][i].get_capacity()
            difference = number_of_students - room_capacity
            if difference > 0:
                malus_points += difference

    # gebruik van avondslot (5)
    schedule_evening = schedule.loc[(schedule["time"] == 17) & schedule["activity"]]
    malus_points += 5 * len(schedule_evening.index)

    # vakconflicten (1)
    schedule_exploded = schedule.explode("students")
    schedule_conflicts = schedule_exploded[["students", "day", "time", "activity"]].groupby(["students", "day", "time"]).count()

    for i in schedule_conflicts.index:
        if schedule_conflicts["activity"][i] > 1:
            malus_points += (schedule_conflicts["activity"][i] - 1)
    schedule_conflicts.to_csv("students.csv")

    # één tussenslot (1) of twee tussensloten (3)
    previous_student = ("dummy_name", "dummy_day", "dummy_time")
    for row in schedule_conflicts.index:
        if row[0:2] == previous_student[0:2]:
            if abs(row[2] - previous_student[2]) == 4:
                malus_points += 1
            if abs(row[2] - previous_student[2]) == 6:
                malus_points += 3
        previous_student = row

    return schedule, malus_points
