import pandas as pd 

def list_to_df(roomslots):
    df = pd.DataFrame(columns = ["day", "time", "room", "activity"])
    for slot in roomslots:
<<<<<<< HEAD
<<<<<<< HEAD
        df = df.append({"day" : slot.get_day(), "time" : slot.get_time(), "room" : slot.get_room(), "activity" : slot.get_activity}, ignore_index = True)
=======
=======
>>>>>>> 955b19f495e23434b6fa4b239d9d6e65d6f10053
        if not slot.get_activity():
            df = df.append({"day" : slot.get_day(), "time" : slot.get_time(), "room" : slot.get_room(), "activity" : "No Activity"}, ignore_index = True)
        else:
            df = df.append({"day" : slot.get_day(), "time" : slot.get_time(), "room" : slot.get_room(), "activity" : slot.get_activity()}, ignore_index = True)
<<<<<<< HEAD
>>>>>>> 955b19f495e23434b6fa4b239d9d6e65d6f10053
=======
>>>>>>> 955b19f495e23434b6fa4b239d9d6e65d6f10053
    return df
