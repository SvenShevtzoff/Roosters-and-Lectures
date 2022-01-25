# =============================================================================
# courses.py with classes course and courses
# =============================================================================

class Course:

    def __init__(self, name):
        self._name = name
        self._activities = set()
        self._students = []

    def add_activity(self, activity):
        """Adds a new activity object to the course object"""
        self._activities.append(activity)

    def add_student(self, student):
        """Adds student object to the course object"""
        self._students.append(student)

    def add_students_to_activities(self):
        """Adds students objects to activty objects"""
        for activity in self._activities:
            activity.set_students(self._students)

    def __str__(self):
        return f"{self._name}"


class Courses:

    def __init__(self, courses):
        self._courses_dict = courses

    def list(self):
        """Returns a list of the courses obj"""
        return list(self._courses_dict.values())

    def single(self, course):
        """Returns a single course object"""
        return self._courses_dict[course]

    def add_students_to_activities_per_course(self):
        """Adds students objects to activity objects per course object"""
        for course in self.list():
            course.add_students_to_activities()
