class Room:

    def __init__(self, roomnumber, capacity):
        self._roomnumber = roomnumber
        self._capacity = capacity
    
    def get_capacity(self):
        return self._capacity


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


class Zaalslot:

    def __init__(self, day, time, room, activity=None):
        self._day = day
        self._time = time
        self._room = room
        self._activity = activity
    
    def get_activity(self):
        return self._activity
    
    def set_activity(self, activity):
        self.activity = activity
    
    def __str__(self):
        return f"Day: {self._day}, Time: {self._time}, Room: {self._room}, Acitivity: {self._activity}"
