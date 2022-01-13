class Room:

    def __init__(self, roomnumber, capacity):
        self._roomnumber = roomnumber
        self._capacity = capacity

    def get_roomnumber(self):
        return self._roomnumber

    def get_capacity(self):
        return self._capacity

    def __str__(self):
        return self._roomnumber


class Course:

    def __init__(self, name, num_of_students=0):
        self._name = name
        self._num_of_students = num_of_students
        self._activities = []
        self._students = []

    def get_name(self):
        return self._name

    def get_num_of_students(self):
        return self._num_of_students

    def add_student(self):
        self._num_of_students += 1
    
    def add_activity(self, activity):
        self._activities.append(activity)
    
    def get_activities(self):
        return self._activities

    def get_students(self):
        return self._students

    def add_student(self, student):
        self._students.append(student)

    def __str__(self):
        return f"{self._name}: {self._num_of_students} student(s)"


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

    def get_course(self):
        return self._course

    def __str__(self):
        return f"{self._kind} {self._course} {self._max_stud}"


class Roomslot:

    def __init__(self, day, time, room, activity=None):
        self._day = day
        self._time = time
        self._room = room
        self._activity = activity

    def get_day(self):
        return self._day

    def get_time(self):
        return self._time

    def get_room(self):
        return self._room

    def get_activity(self):
        return self._activity

    def get_day(self):
        return self._day

    def get_time(self):
        return self._time

    def get_course(self):
        return self._activity.get_course()

    def set_activity(self, activity):
        self._activity = activity

    def __str__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"

    def __repr__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"


class Student:

    def __init__(self, last_name, first_name, student_number, courses):
        self._last_name = last_name
        self._first_name = first_name
        self._student_number = student_number
        self._courses = courses