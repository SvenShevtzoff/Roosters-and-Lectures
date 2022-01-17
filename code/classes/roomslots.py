class Roomslot:

    def __init__(self, day, time, room, activity=None):
        self._day = day
        self._time = time
        self._room = room
        self._activity = activity
        self._visualized = False

    def get_day(self):
        return self._day

    def get_time(self):
        return self._time

    def get_room(self):
        return self._room

    def get_activity(self):
        return self._activity

    def get_course(self):
        return self._activity.get_course()

    def set_activity(self, activity):
        self._activity = activity

    def is_visualized(self):
        return self._visualized

    def set_visualized(self): 
        self._visualized = True

    def __str__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"

    def __repr__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"


class Roomslots:

    def __init__(self, roomslots):
        self._roomslots_dict = roomslots

    def get_dict(self):
        return self._roomslots_dict

    def get_list(self):
        self._roomslots_list = []
        for slot in list(self._roomslots_dict.values()):
            self._roomslots_list.append(slot)
        return self._roomslots_list
