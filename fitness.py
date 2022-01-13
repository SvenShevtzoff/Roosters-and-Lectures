import pandas as pd


def dict_to_df(roomslots):
    df = pd.DataFrame(columns=["day", "time", "room", "activity"])
    for slot in roomslots.get_list():
        if not slot.get_activity():
            df = df.append({
                "day": slot.get_day(),
                "time": slot.get_time(),
                "room": slot.get_room(),
                "activity": "No Activity"}, ignore_index=True)
        else:
            df = df.append({
                "day": slot.get_day(),
                "time": slot.get_time(),
                "room": slot.get_room(),
                "activity": slot.get_activity()}, ignore_index=True)
    return df


def fitness_function(schedule):
    pass
