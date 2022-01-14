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
                "students": None}
                , ignore_index=True)
        else:
            students = []
            for student in slot.get_course().get_students():
                students.append(student.__str__())
            df = df.append({
                "day": slot.get_day(),
                "time": slot.get_time(),
                "room": slot.get_room(),
                "activity": slot.get_activity(),
                "students": students}
                , ignore_index=True)
    return df


def fitness_function(schedule):
    # print(schedule)
    malus_points = 0
    # aantal studenten groter dan maximum toegestaan in de zaal (1)
    # for i in schedule.index:
    #     if schedule["activity"][i]:
    #         max_students_in_activity = schedule["activity"][i].get_max_stud()
    #         room_capacity = schedule["room"][i].get_capacity()
    #         difference = max_students_in_activity - room_capacity
    #         if difference > 0:
    #             malus_points += difference

    # print(malus_points)

    # # gebruik van avondslot (5)
    # schedule_evening = schedule.loc[(schedule["time"] == 17) & schedule["activity"]]
    # malus_points += 5 * len(schedule_evening.index)

    # print(malus_points)

    # # vakconflicten (1)
    schedule_exploded = schedule.explode("students")

    schedule_conflicts = schedule_exploded[["students", "day", "time", "activity"]].groupby(["students", "day", "time"]).count()

    # for i in schedule_conflicts.index:
    #     if schedule_conflicts["activity"][i] > 1:
    #         malus_points += (schedule_conflicts["activity"][i] - 1)
    # schedule_conflicts.to_csv("students.csv")
    # print(malus_points)

    # # één tussenslot (1)
    # previous_student = ("dummy_name", "dummy_day", "dummy_time")
    # for row in schedule_conflicts.index:
    #     if row[0:2] == previous_student[0:2]:
    #         if abs(row[2] - previous_student[2]) == 4:
    #             malus_points += 1
    #         if abs(row[2] - previous_student[2]) == 6:
    #             malus_points += 3
    #     previous_student = row

    # print(schedule_conflicts.head(10))
    # print(malus_points)

    # tryout
    tryout_df = schedule_conflicts.head(10)
    print(tryout_df)

    previous_student = ("dummy_name", "dummy_day", "dummy_time")
    for row in tryout_df.index:
        if row[0:2] == previous_student[0:2]:
            if abs(row[2] - previous_student[2]) == 4:
                malus_points += 1
            if abs(row[2] - previous_student[2]) == 6:
                malus_points += 3
        print(malus_points)
        previous_student = row
    # twee tussensloten (3)

    return malus_points
