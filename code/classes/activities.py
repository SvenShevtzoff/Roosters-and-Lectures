import random
from math import ceil


class Activity:

    def __init__(self, unique_id, kind, course, max_stud=0):
        self._unique_id = unique_id
        self._kind = kind
        self._course = course
        self._max_stud = max_stud
        self._roomslot = None
        self._students = {}

    def unique_id(self):
        return self._unique_id

    def kind(self):
        return self._kind

    def roomslot(self):
        return self._roomslot

    def set_roomslot(self, slot):
        slot.set_activity(self)
        self._roomslot = slot

    def max_stud(self):
        return self._max_stud

    def course(self):
        return self._course

    def set_students(self, students):
        for student in students:
            self._students[str(student)] = student
        for student in students:
            student.add_activity(self)
    
    def add_student(self, student):
        self._students[str(student)] = student
    
    def remove_student(self, student):
        self._students.pop(str(student))

    def students(self):
        return self._students

    def num_of_enrolled_students(self):
        return len(self._students)
    
    def split_into(self, amount):
        new_activities = []
        # creating new activities
        for i in range(1, amount):
            new_activities.append(Activity(f"{self._unique_id}.{i}", self._kind, self._course, self._max_stud))
        
        # calculating how many students to move
        amount_students_per_activity = ceil(self.num_of_enrolled_students() / amount)

        # moving students to new activities
        for new_activity in new_activities:
            new_students = random.sample(list(self._students.values()), amount_students_per_activity)
            for new_student in new_students:
                # removing from current activity
                new_student.remove_activity(self)
                self.remove_student(new_student)

                # adding to new activity
                new_student.add_activity(new_activity)
                new_activity.add_student(new_student)

        return new_activities


    def __str__(self):
        return f"{self._kind} {self._course} {self._unique_id}"


class Activities:

    def __init__(self, activities):
        if type(activities) == list:
            self._activities_dict = {}
            for activity in activities:
                self._activities_dict[str(activity)] = activity
        else:
            self._activities_dict = activities

    def dict(self):
        return self._activities_dict

    def list(self):
        self._activities_list = []
        for activity in list(self._activities_dict.values()):
            self._activities_list.append(activity)
        return self._activities_list

    def add_activity(self, activity):
        self._activities_dict[str(activity)] = activity
        # if self._activities_dict[str(activity)]:
        #     self._activities_dict[f"{str(activity)} 2"]
        # elif self._activities_dict[f"{str(activity)} 2"]:
        #     self._activities_dict[f"{str(activity)} 3"]
        # else:
        #     self._activities_dict[str(activity)] = activity

    def length(self):
        return len(self._activities_dict)
