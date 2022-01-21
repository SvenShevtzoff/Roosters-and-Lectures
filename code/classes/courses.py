class Course:

    def __init__(self, name):
        self._name = name
        self._activities = []
        self._students = []

    def name(self):
        return self._name

    def num_of_students(self):
        return len(self._students)

    def add_activity(self, activity):
        self._activities.append(activity)

    def activities(self):
        return self._activities

    def students(self):
        return self._students

    def add_student(self, student):
        self._students.append(student)

    def add_students_to_activities(self):
        for activity in self._activities:
            activity.set_students(self._students)

    def __str__(self):
        return f"{self._name}"


class Courses:

    def __init__(self, courses):
        self._courses_dict = courses

    def dict(self):
        return self._courses_dict

    def list(self):
        self._courses_list = []
        for course in list(self._courses_dict.values()):
            self._courses_list.append(course)
        return self._courses_list

    def single(self, course):
        return self._courses_dict[course]

    def add_students_to_activities_per_course(self):
        for course in self.list():
            course.add_students_to_activities()
