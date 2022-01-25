# =============================================================================
# activities.py with classes activity and activities
# =============================================================================

import random
import copy
from math import ceil


class Activity:

    def __init__(self, unique_id, kind, course, max_stud=0):
        self._unique_id = unique_id
        self._kind = kind
        self._course = course
        self._max_stud = max_stud
        self._roomslot = None
        self._students = set()

    def copy(self):
        new = copy.copy(self)
        new._kind = copy.copy(self._kind)
        new._course = copy.copy(self._course)
        new._max_stud = copy.copy(self._max_stud)
        new._roomslot = copy.copy(self._roomslot)
        new._students = copy.copy(self._students)

        return new

    def unique_id(self):
        """Returns unique_id of activity"""
        return self._unique_id

    def kind(self):
        """Returns kind of the activity (with kind in {practicum, lecture, tutorial})"""
        return self._kind

    def roomslot(self):
        """Returns roomslot object of activity"""
        return self._roomslot

    def set_roomslot(self, slot):
        """Connects a roomslot object to an activity object"""
        slot.set_activity(self)
        self._roomslot = slot

    def max_stud(self):
        """Returns the maximum of students in an activity"""
        return self._max_stud

    def course(self):
        """Returns the couse object of an activity"""
        return self._course

    def set_students(self, students, all_students):
        """Connects a list of students to an activity"""
        for student in students:
            self._students.add(student)
        for student in students:
            all_students.single(student).add_activity(str(self))

    def add_student(self, student_key):
        """Adds a student object to the studentlist of that activtiy"""
        self._students.add(student_key)

    def remove_student(self, student_key):
        """Removes a student object from the studentlist of that activtiy"""
        self._students.remove(student_key)

    def students(self):
        """Returns all student objects from that activity"""
        return self._students

    def num_of_enrolled_students(self):
        """Returns the number of enrolled students"""
        return len(self._students)

    def split_into(self, amount, all_students):
        """Splits the activities in groups that fit the restictions of groupsize"""
        new_activities = []
        # creating new activities
        for i in range(1, amount):
            new_activities.append(Activity(f"{self._unique_id}.{i}", self._kind, self._course, self._max_stud))

        # calculating how many students to move
        amount_students_per_activity = ceil(self.num_of_enrolled_students() / amount)

        # moving students to new activities
        for new_activity in new_activities:
            new_students = random.sample(self._students, amount_students_per_activity)
            for new_student_key in new_students:
                # removing from current activity
                all_students.single(new_student_key).remove_activity(str(self))
                self.remove_student(new_student_key)

                # adding to new activity
                all_students.single(new_student_key).add_activity(str(new_activity))
                new_activity.add_student(new_student_key)

        return new_activities

    def __str__(self):
        return f"{self._kind} {self._course} {self._unique_id}"

    def __repr__(self):
        return f"{self._kind} {self._course} {self._unique_id}"


class Activities:

    def __init__(self, activities):
        if type(activities) == list:
            self._activities_dict = {}
            for activity in activities:
                self._activities_dict[str(activity)] = activity
        else:
            self._activities_dict = activities

    def list(self):
        """Returns a list of the activtities"""
        return list(self._activities_dict.values())

    def dict(self):
        return self._activities_dict

    def single(self, activity_key):
        """Returns an Activity object, given its key"""
        return self._activities_dict[activity_key]

    def add_activity(self, activity):
        """Add a new activity"""
        self._activities_dict[str(activity)] = activity

    def copy(self):
        new = copy.copy(self)
        new._activities_dict = {}
        for activity in self.list():
            new._activities_dict[str(activity)] = activity.copy()
        return new
