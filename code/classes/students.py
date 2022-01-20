class Student:

    def __init__(self, last_name, first_name, student_number, courses):
        self._last_name = last_name
        self._first_name = first_name
        self._student_number = student_number
        self._courses = courses
        self._activities = set()

    def name(self):
        return f"{self._first_name} {self._last_name}"

    def courses(self):
        return self._courses

    def add_activity(self, activity):
        self._activities.add(activity)
    
    def remove_activity(self, activity):
        self._activities.remove(activity)

    def activities(self):
        return list(self._activities)

    def __str__(self):
        return f"{self._first_name} {self._last_name}"

    def __repr__(self):
        return f"{self._first_name} {self._last_name}"


class Students:

    def __init__(self, students):
        self._students_dict = students

    def dict(self):
        return self._students_dict

    def list(self):
        self._students_list = []
        for student in list(self._students_dict.values()):
            self._students_list.append(student)

        return self._students_list
