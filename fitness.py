import pandas as pd


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
            df = df.append({
                "day": slot.get_day(),
                "time": slot.get_time(),
                "room": slot.get_room(),
                "activity": slot.get_activity(),
                "students": slot.get_course().get_students()}
                , ignore_index=True)
    return df


def fitness_function(schedule):
    print(schedule)
    malus_points = 0
    # aantal studenten groter dan maximum toegestaan in de zaal
    for i in schedule.index:
        if schedule["activity"][i]:
            max_students_in_activity = schedule["activity"][i].get_max_stud()
            room_capacity = schedule["room"][i].get_capacity()
            difference = max_students_in_activity - room_capacity
            if difference > 0:
                malus_points += difference

    # gebruik van avondslot
    schedule_evening = schedule.loc[(schedule["time"] == 17) & schedule["activity"]]
    malus_points += 5 * len(schedule_evening.index)

    # vakconflicten
    

    # één tussenslot


    # twee tussensloten

    pass

# les van 17 (5)
# niet in te roosteren studenten (1)
# vakconflict (1)
# 1 tussenuur (1)
# 2 tussenuur(3)
# geen 3 sloten
