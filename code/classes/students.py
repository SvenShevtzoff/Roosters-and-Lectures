class Student:

    def __init__(self, last_name, first_name, student_number, courses):
        self._last_name = last_name
        self._first_name = first_name
        self._student_number = student_number
        self._courses = courses

    def get_name(self):
        return f"{self._first_name} {self._last_name}"

    def __str__(self):
        return f"{self._first_name} {self._last_name}"

    def __repr__(self):
        return f"{self._first_name} {self._last_name}"


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
