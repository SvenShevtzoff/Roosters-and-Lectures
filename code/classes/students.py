# =============================================================================
# student.py with classes student and students
# =============================================================================

class Student:

    def __init__(self, last_name, first_name, student_number, courses):
        self._last_name = last_name
        self._first_name = first_name
        self._student_number = student_number
        self._courses = courses
        self._activities = set()

    def name(self):
        """Returns name and surname of student"""
        return f"{self._first_name} {self._last_name}"

    def courses(self):
        """Returns the course objects of a student"""
        return self._courses

    def add_activity(self, activity):
        """Adds an activity object to the activity set of the student"""
        self._activities.add(activity)
    
    def remove_activity(self, activity):
        """Removes an activity object from the activity set of the student """
        self._activities.remove(activity)

    def activities(self):
        """Returns a list with activity objects form the student"""
        return list(self._activities)

    def __str__(self):
        return f"{self._first_name} {self._last_name}"

    def __repr__(self):
        return f"{self._first_name} {self._last_name}"


class Students:

    def __init__(self, students):
        self._students_dict = students

    def dict(self):
        """Returns a dictionary of the students"""
        return self._students_dict

    def list(self):
        """Returns a list of the students"""
        self._students_list = []
        for student in list(self._students_dict.values()):
            self._students_list.append(student)

        return self._students_list
