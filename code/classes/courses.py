class Course:

    def __init__(self, name, num_of_lectures, num_of_tutorials=0, num_of_practica=0):
        self._name = name
        self._activities = []
        self._students = []
        self._num_of_lectures = num_of_lectures
        self._num_of_tutorials = num_of_tutorials
        self._num_of_practica = num_of_practica

    def get_name(self):
        return self._name

    def get_num_of_tutorials(self):
        return self._num_of_tutorials

    def get_num_of_practica(self):
        return self._num_of_practica

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
        return f"{self._name}: {len(self._students)} student(s)"

    def add_students_to_activities(self):
        for activity in self._activities:
            activity.set_students(self._students)


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

    def add_students_to_activities(self):
        for course in self.get_list():
            course.add_students_to_activities()
