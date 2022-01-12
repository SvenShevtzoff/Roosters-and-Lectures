class Room:

    def __init__(self, roomnumber, capacity):
        self._roomnumber = roomnumber
        self._capacity = capacity
    
    def get_capacity(self):
        return self._capacity

    def __str__(self):
        return self._roomnumber


class Activity:
    
    def __init__(self, kind, course, max_stud=0):
        self._kind = kind
        self._course = course
        self._max_stud = max_stud
        self._roomslot = None

    def get_roomslot(self):
        return self._roomslot

    def set_roomslot(self, slot):
        slot.set_activity(self)
        self._roomslot = slot

    def get_max_stud(self):
        return self._max_stud

    def __str__(self):
        return f"{self._kind} {self._course}"


class Roomslot:

    def __init__(self, day, time, room, activity=None):
        self._day = day
        self._time = time
        self._room = room
        self._activity = activity

    def get_room(self):
        return self._room

    def get_activity(self):
        return self._activity
    
    def get_day(self):
        return self._day
    
    def get_time(self):
        return self._time

    
    def set_activity(self, activity):
        self._activity = activity
    
    def __str__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"
