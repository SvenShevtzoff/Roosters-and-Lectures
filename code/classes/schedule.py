# =============================================================================
# schedule.py with classe schedule
# =============================================================================

from re import L
from code.classes.activities import Activity
from code.classes.roomslots import Roomslot
from collections import defaultdict
from code.visualize import visualize as vis
import matplotlib.pyplot as plt
from math import ceil


class Schedule:

    def __init__(self, roomslots, activities, students):
        self._roomslots = roomslots
        self._activities = activities
        self._students = students

    def roomslots(self):
        """Returns roomslot objects from the schedule"""
        return self._roomslots

    def activities(self):
        """Returns activity objects form the schedule"""
        return self._activities

    def students(self):
        """Returns student objects from the schedule"""
        return self._students

    def course_schedule(self, course):
        """Returns a schedule for a given course"""
        return [x.roomslot() for x in self._activities.list() if course == x.course().name()]

    def room_schedule(self, room):
        """Returns a schedule for a given room"""
        return [x for x in self._roomslots.list() if str(room) == x.room().roomnumber() and x.activity() is not None]

    def student_schedule(self, student):
        """Returns a schedule for a given student"""
        schedule = []
        for x in self._activities.list():
            student_names = [i.name() for i in x.students()]
            if student in student_names:
                schedule.append(x.roomslot())
        return schedule

    def divide_students(self):
        """Divides students over multiple of the same activity to comply with the max students for an activity"""
        all_activities = self.activities()
        activities_to_add = []

        for activity in all_activities.list():
            if activity.kind() != "Lecture":
                amount = ceil(activity.num_of_enrolled_students() / activity.max_stud())
                if amount > 1:
                    activities_to_add = activities_to_add + activity.split_into(amount, self.students())

        for activity in activities_to_add:
            all_activities.add_activity(activity)

    def conflicts_student(self, student_to_check):
        """Returns all the conflicts of a student"""
        dictionary = defaultdict(list)
        for activity in self._activities.list():
            students = activity.students()
            if student_to_check in students:
                dictionary[f"{activity.roomslot().day()}, {activity.roomslot().time()}"].append(activity.roomslot())

        return [x for x in dictionary.values() if len(x) > 1]

    def conflicts_course(self, course_name):
        """Returns all the conflicts of a course"""
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

    def merge(self, activity_to_merge):
        """Merges an activity with other activities, if any"""
        all_activities = self.activities()
        activities_to_merge = []

        # find all activities to merge
        for activity in all_activities.list():
            if activity.kind() == activity_to_merge.kind() and activity.name() == activity_to_merge.name():
                activities_to_merge.append(activity)

        print(activities_to_merge)

        if len(activities_to_merge) > 1:
            # if more than one group, find all students in these groups
            students_keys = []
            for activity in activities_to_merge:
                print(activity.students())
                students_keys.extend(activity.students())
            print(students_keys)
            activity_to_keep = activities_to_merge[0]
            activity_to_keep.set_students(students_keys, self.students())
            activity_to_keep.set_id_to_1()
            activities_to_remove = activities_to_merge[:1]

        for activity in activities_to_remove:
            all_activities.remove_activity(activity)
        
    def fitness(self):
        """Calculates the fitness of the schedule"""
        gapdict = self.empty_roomslot_check()
        malus_points = gapdict[1] * 1
        malus_points += gapdict[2] * 3
        malus_points += gapdict[3] * 1000
        malus_points += self.exceed_max_activity_check()
        malus_points += self.max_roomsize_check()
        malus_points += self.use_17_slot_check()
        malus_points += self.course_conflict_check()

        # print(f"Pandapunten: {malus_points}")
        return malus_points

    def max_roomsize_check(self):
        """Calculates the malus points generated by the exceeding of maximum capacity"""
        malus_points = 0
        for slot in self.roomslots().list():
            if slot.activity():
                room_capacity = slot.room().capacity()
                number_of_students = slot.activity().num_of_enrolled_students()
                difference = number_of_students - room_capacity
                if difference > 0:
                    malus_points += difference

        return malus_points

    def exceed_max_activity_check(self):
        """Checks if the maximum amount of students in an tutorial/practicum is not exceeded"""
        malus_points = 0
        for activity in self.activities().list():
            if activity.kind() != "Lecture":
                if activity.num_of_enrolled_students() > activity.max_stud():
                    malus_points += 1000

        return malus_points

    def use_17_slot_check(self):
        """Calculates the malus points generated by the use of the 17-19 timeslot"""
        malus_points = 0
        for slot in self.roomslots().list():
            if slot.time() == 17 and slot.activity():
                malus_points += 5

        return malus_points

    def course_conflict_check(self):
        """Calculates the malus points generated by the course conflicts of a student"""
        malus_points = 0
        for student in self.students().list():
            for conflict in self.conflicts_student(student):
                malus_points += len(conflict) - 1

        return malus_points

    def empty_roomslot_check(self):
        """Calculates the malus points generated by the students having gapslots"""
        gapdict = {1: 0, 2: 0, 3: 0}
        for student in self.students().list():
            students_activities_keys = student.activities()
            for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
                students_activities_per_day = []
                for activity_key in students_activities_keys:
                    if self.activities().single(activity_key).roomslot().day() == day:
                        students_activities_per_day.append(self.activities().single(activity_key))
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
        """Generates a visualisation per room"""
        for room in rooms.list():
            vis.visualize_room(self, room)
            plt.savefig(f"doc/output/schedule_{str(room)}.png")
