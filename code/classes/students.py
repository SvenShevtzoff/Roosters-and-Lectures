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

    def std_number(self):
        """Returns student number of student"""
        return self._student_number

    def add_activity(self, activity_key):
        """Adds an activity object to the activity set of the student"""
        self._activities.add(activity_key)

    def remove_activity(self, activity_key):
        """Removes an activity object from the activity set of the student"""
        self._activities.remove(activity_key)

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

    def list(self):
        """Returns a list of the students"""
        return list(self._students_dict.values())

    def single(self, student_key):
        """Takes a Student object out of the Students dictionary, given its key"""
        return self._students_dict[student_key]
