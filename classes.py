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


class Rooms:

    def __init__(self, rooms):
        self._rooms_dict = rooms

    def get_dict(self):
        return self._rooms_dict

    def get_list(self):
        self._rooms_list = []
        for room in list(self._rooms_dict.values()):
            self._rooms_list.append(room)
        return self._rooms_list


class Course:

    def __init__(self, name):
        self._name = name
        self._activities = []
        self._students = []

    def get_name(self):
        return self._name

    def get_num_of_students(self):
        return len(self._students)

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


class Courses:

    def __init__(self, courses):
        self._courses_dict = courses

    def get_dict(self):
        return self._courses_dict

    def get_list(self):
        self._courses_list = []
        for course in list(self._courses_dict.values()):
            self._courses_list.append(course)
        return self._courses_list
    
    def get_single(self, course):
        return self._courses_dict[course]


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


class Activities:

    def __init__(self, activities):
        self._activities_dict = activities

    def get_dict(self):
        return self._activities_dict

    def get_list(self):
        self._activities_list = []
        for activity in list(self._activities_dict.values()):
            self._activities_list.append(activity)
        return self._activities_list

    def length(self):
        return len(self._activities_dict)


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

    def get_course(self):
        return self._activity.get_course()

    def set_activity(self, activity):
        self._activity = activity

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


class Student:

    def __init__(self, last_name, first_name, student_number, courses):
        self._last_name = last_name
        self._first_name = first_name
        self._student_number = student_number
        self._courses = courses


class Students:

    def __init__(self, students):
        self._students_dict = students

    def get_dict(self):
        return self._students_dict

    def get_list(self):
        self._students_list = []
        for student in list(self._students_dict.values()):
            self._students_list.append(student)
        return self._students_list
