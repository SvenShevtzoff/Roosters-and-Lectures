# =============================================================================
# courses.py with classes course and courses
# =============================================================================

class Course:

    def __init__(self, name):
        self._name = name
        self._activities = set()
        self._students = set()

    def add_activity(self, activity):
        """Adds a new activity object to the course object"""
        self._activities.add(str(activity))

    def add_student(self, student):
        """Adds student object to the course object"""
        self._students.add(student.std_number())

    def add_students_to_activities(self, all_activities, all_students):
        """Adds students objects to activty objects"""
        for activity_key in self._activities:
            all_activities.single(activity_key).set_students(self._students, all_students)

    def __str__(self):
        return f"{self._name}"


class Courses:

    def __init__(self, courses):
        self._courses_dict = courses

    def list(self):
        """Returns a list of the courses obj"""
        return list(self._courses_dict.values())

    def single(self, course_key):
        """Returns a single course object"""
        return self._courses_dict[course_key]

    def add_students_to_activities_per_course(self, all_activities, all_students):
        """Adds students objects to activity objects per course object"""
        for course in self.list():
            course.add_students_to_activities(all_activities, all_students)
