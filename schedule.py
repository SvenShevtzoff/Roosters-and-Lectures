from classes import Room, Rooms, Course, Courses, Roomslot, Roomslots, Activity, Activities, Student, Students
import pandas as pd


class Schedule:

    def __init__(self, courses, activities, roomslots, students):
        self._roomslots = roomslots
        self._students = students
        self._courses = courses
        self._activities = activities

    def course_schedule(self, course):
        return [x.get_roomslot() for x in self._activities.get_list() if course == x.get_course()]
    
    def room_schedule(self, room):
        return [x for x in self._roomslots.get_list() if room == x.get_room().get_roomnumber()]

    def student_schedule(self, student):
        #niet zeker of deze werkt
        return [x.get_roomslot() for x in self._activities.get_list() if student in x.get_students()]

    def day_schedule(self, day):
        return [x for x in self._roomslots.get_list() if day == x.get_day()]

    def time_schedule(self, time):
        return [x for x in self._roomslots.get_list() if time == x.get_time()]
    
    # def empty_schedule(self):
    #     return [x.get_roomslot() for x in self._activities.get_list()]