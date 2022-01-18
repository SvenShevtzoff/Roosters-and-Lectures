class Activity:

    def __init__(self, kind, course, max_stud=0):
        self._kind = kind
        self._course = course
        self._max_stud = max_stud
        self._roomslot = None
        self._students = {}

    def get_kind(self):
        return self._kind

    def get_roomslot(self):
        return self._roomslot

    def set_roomslot(self, slot):
        slot.set_activity(self)
        self._roomslot = slot

    def get_max_stud(self):
        return self._max_stud

    def get_course(self):
        return self._course

    def set_students(self, students):
        for student in students:
            self._students[str(student)] = student
        for student in students:
            student.add_activity(self)

    def get_students(self):
        return self._students

    def get_num_of_enrolled_students(self):
        return len(self._students)

    def __str__(self):
        return f"{self._kind} {self._course}"


class Activities:

    def __init__(self, activities):
        if type(activities) == list:
            self._activities_dict = {}
            for activity in activities:
                self._activities_dict[str(activity)] = activity
        else:
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
