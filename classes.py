class Room:

    def __init__(self, roomnumber, capacity):
        self._roomnumber = roomnumber
        self._capacity = capacity
    
    def get_capacity(self):
        return self._capacity

    def __str__(self):
        return self._roomnumber


class Lecture:
    
    def __init__(self, course, e_stud=0):
        self._course = course
        self._e_stud = e_stud
    
    def __str__(self):
        return f"Lecture {self._course}"


class Tutorial:
    
    def __init__(self, course, max_stud=0):
        self._course = course
        self._e_stud = max_stud
    
    def __str__(self):
        return f"Tutorial {self._course}"


class Practicum:
    
    def __init__(self, course, max_stud=0):
        self._course = course
        self._e_stud = max_stud
    
    def __str__(self):
        return f"Practicum {self._course}"


class Roomslot:

    def __init__(self, unique_id, day, time, room, activity=None):
        self._unique_id = unique_id
        self._day = day
        self._time = time
        self._room = room
        self._activity = activity
    
    def get_unique_id(self):
        return self._unique_id

    def get_activity(self):
        return self._activity
    
    def set_activity(self, activity):
        self._activity = activity
    
    def __str__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"
