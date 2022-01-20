from classes.activities import Activity
from classes.roomslots import Roomslot
from collections import defaultdict
from visualize import visualize_room
import matplotlib.pyplot as plt


class Schedule:

    def __init__(self, roomslots, activities, students):
        self._roomslots = roomslots
        self._activities = activities
        self._students = students

    def get_roomslots(self):
        return self._roomslots

    def get_activities(self):
        return self._activities

    def get_students(self):
        return self._students

    def course_schedule(self, course):
        return [x.get_roomslot() for x in self._activities.get_list() if course == x.get_course().get_name()]

    def room_schedule(self, room):
        return [x for x in self._roomslots.get_list() if str(room) == x.get_room().get_roomnumber() and x.get_activity() is not None]

    def student_schedule(self, student):
        schedule = []
        for x in self._activities.get_list():
            student_names = [i.get_name() for i in x.get_students()]
            if student in student_names:
                schedule.append(x.get_roomslot())
        return schedule

    def day_schedule(self, day):
        return [x for x in self._roomslots.get_list() if day == x.get_day() and x.get_activity() is not None]

    def time_schedule(self, time):
        return [x for x in self._roomslots.get_list() if time == x.get_time() and x.get_activity() is not None]

    def get_conflicts_student(self, student_to_check):
        dictionary = defaultdict(list)
        student_to_check = student_to_check.get_name()
        for activity in self._activities.get_list():
            students = activity.get_students()
            if student_to_check in students:
                dictionary[f"{activity.get_roomslot().get_day()}, {activity.get_roomslot().get_time()}"].append(activity.get_roomslot())

        return [x for x in dictionary.values() if len(x) > 1]

    def get_conflicts_course(self, course_name):
        dictionary = {}
        course_activities = []
        for activity in self._activities.get_list():
            if str(activity.get_course()) == course_name:
                course_activities = activity.get_course().get_activities()
                break

        for activity in course_activities:
            if f"{activity.get_roomslot().get_day()}, {activity.get_roomslot().get_time()}" in dictionary:
                dictionary[f"{activity.get_roomslot().get_day()}, {activity.get_roomslot().get_time()}"].append(activity.get_roomslot())
            else:
                dictionary[f"{activity.get_roomslot().get_day()}, {activity.get_roomslot().get_time()}"] = [activity.get_roomslot()]

        return [activity for activity in dictionary.values() if len(activity) > 1]

    def fitness(self):
        malus_points = self.max_roomsize_check()
        malus_points += self.use_17_slot_check()
        malus_points += self.course_conflict_check()
        malus_points += self.empty_roomslot_check()
        print(f"Pandapunten: {malus_points}")

        return malus_points

    def max_roomsize_check(self):
        '''aantal studenten groter dan maximum toegestaan in de zaal (1)'''
        malus_points = 0
        for slot in self.get_roomslots().get_list():
            if slot.get_activity():
                room_capacity = slot.get_room().get_capacity()
                number_of_students = slot.get_activity().get_num_of_enrolled_students()
                difference = number_of_students - room_capacity
                if difference > 0:
                    malus_points += difference

        return malus_points

    def use_17_slot_check(self):
        '''gebruik van avondslot (5)'''
        malus_points = 0
        for slot in self.get_roomslots().get_list():
            if slot.get_time() == 17 and slot.get_activity():
                malus_points += 5

        return malus_points

    def course_conflict_check(self):
        '''vakconflicten (1)'''
        malus_points = 0
        for student in self.get_students().get_list():
            for conflict in self.get_conflicts_student(student):
                malus_points += len(conflict) - 1

        return malus_points

    def empty_roomslot_check(self):
        '''één tussenslot (1) of twee tussensloten (3)'''
        malus_points = 0
        for student in self.get_students().get_list():
            students_activities = student.get_activities()
            for activity in students_activities:
                for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
                    students_activities_per_day = [activity for activity in students_activities if str(activity.get_roomslot().get_day()) == day]
                    students_activities_sorted = sorted(students_activities_per_day, key=lambda x: x.get_roomslot().get_time(), reverse=True)
                    # dummy activity
                    previous_activity = Activity("dummy_kind", "dummy_course")

                    # 0 because the only time options are 9, 11, 13, 15 and 17 so now the
                    # difference is never 4 or 6 (so we never wrongfully get a malus point)
                    previous_activity.set_roomslot(Roomslot("dummy_day", 0, "dummy_room"))
                    for activity in students_activities_sorted:
                        current_time = int(activity.get_roomslot().get_time())
                        previous_time = previous_activity.get_roomslot().get_time()
                        if abs(current_time - previous_time) == 4:
                            malus_points += 1
                        if abs(current_time - previous_time) == 6:
                            malus_points += 3
                        previous_activity = activity
                
                    

        return malus_points

    def visualize_by_room(self, rooms):
        for room in rooms.get_list():
            visualize_room(self, room)
            plt.savefig(f"../doc/output/schedule_{str(room)}.png")
