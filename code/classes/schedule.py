from classes.activities import Activity
from classes.roomslots import Roomslot
from collections import defaultdict
from visualize import visualize_room
import matplotlib.pyplot as plt
from math import ceil
import copy

class Schedule:

    def __init__(self, roomslots, activities, students):
        self._roomslots = roomslots
        self._activities = activities
        self._students = students

    def roomslots(self):
        return self._roomslots

    def activities(self):
        return self._activities

    def students(self):
        return self._students

    def course_schedule(self, course):
        return [x.roomslot() for x in self._activities.list() if course == x.course().name()]

    def room_schedule(self, room):
        return [x for x in self._roomslots.list() if str(room) == x.room().roomnumber() and x.activity() is not None]

    def student_schedule(self, student):
        schedule = []
        for x in self._activities.list():
            student_names = [i.name() for i in x.students()]
            if student in student_names:
                schedule.append(x.roomslot())
        return schedule

    def divide_students(self):
        all_activities = self.activities()
        activities_to_add = []

        for activity in all_activities.list():
            if activity.kind() != "Lecture":
                amount = ceil(activity.num_of_enrolled_students() / activity.max_stud())
                if amount > 1:
                    new_activities = activity.split_into(amount)

                    for activity in new_activities:
                        activities_to_add.append(activity)
    
        for activity in activities_to_add:
            all_activities.add_activity(activity)

    def conflicts_student(self, student_to_check):
        dictionary = defaultdict(list)
        student_to_check = student_to_check.name()
        for activity in self._activities.list():
            students = activity.students()
            if student_to_check in students:
                dictionary[f"{activity.roomslot().day()}, {activity.roomslot().time()}"].append(activity.roomslot())

        return [x for x in dictionary.values() if len(x) > 1]

    def conflicts_course(self, course_name):
        dictionary = {}
        course_activities = []
        for activity in self._activities.list():
            if str(activity.course()) == course_name:
                course_activities = activity.course().activities()
                break

        for activity in course_activities:
            if f"{activity.roomslot().day()}, {activity.roomslot().time()}" in dictionary:
                dictionary[f"{activity.roomslot().day()}, {activity.roomslot().time()}"].append(activity.roomslot())
            else:
                dictionary[f"{activity.roomslot().day()}, {activity.roomslot().time()}"] = [activity.roomslot()]

        return [activity for activity in dictionary.values() if len(activity) > 1]

    def fitness(self):
        gapdict = self.empty_roomslot_check()
        if gapdict[3] > 0:
            print(gapdict[3])
            return -1
        else:
            malus_points = gapdict[1] * 1
            malus_points += gapdict[2] * 3
            malus_points += self.max_roomsize_check()
            malus_points += self.use_17_slot_check()
            malus_points += self.course_conflict_check()

            # print(f"Pandapunten: {malus_points}")
            return malus_points

    def max_roomsize_check(self):
        '''aantal studenten groter dan maximum toegestaan in de zaal (1)'''
        malus_points = 0
        for slot in self.roomslots().list():
            if slot.activity():
                room_capacity = slot.room().capacity()
                number_of_students = slot.activity().num_of_enrolled_students()
                difference = number_of_students - room_capacity
                if difference > 0:
                    malus_points += difference

        return malus_points

    def use_17_slot_check(self):
        '''gebruik van avondslot (5)'''
        malus_points = 0
        for slot in self.roomslots().list():
            if slot.time() == 17 and slot.activity():
                malus_points += 5

        return malus_points

    def course_conflict_check(self):
        '''vakconflicten (1)'''
        malus_points = 0
        for student in self.students().list():
            for conflict in self.conflicts_student(student):
                malus_points += len(conflict) - 1

        return malus_points

    def empty_roomslot_check(self):
        '''één tussenslot (1) of twee tussensloten (3)'''
        gapdict = {1 : 0, 2 : 0, 3 : 0}
        for student in self.students().list():
            students_activities = student.activities()
            for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
                students_activities_per_day = [activity for activity in students_activities if activity.roomslot().day() == day]
                students_activities_sorted = sorted(students_activities_per_day, key=lambda x: x.roomslot().time(), reverse=True)
                # dummy activity
                previous_activity = Activity("dummy_id", "dummy_kind", "dummy_course")

                # 0 because the only time options are 9, 11, 13, 15 and 17 so now the
                # difference is never 4 or 6 (so we never wrongfully get a malus point)
                previous_activity.set_roomslot(Roomslot("dummy_day", 0, "dummy_room"))
                for activity in students_activities_sorted:
                    current_time = int(activity.roomslot().time())
                    previous_time = previous_activity.roomslot().time()
                    if abs(current_time - previous_time) == 4:
                        gapdict[1] += 1
                    if abs(current_time - previous_time) == 6:
                        gapdict[2] += 1
                    if abs(current_time - previous_time) == 8:
                        gapdict[3] += 1
                    previous_activity = activity
        
        return gapdict

    def visualize_by_room(self, rooms):
        for room in rooms.list():
            visualize_room(self, room)
            plt.savefig(f"../doc/output/schedule_{str(room)}.png")