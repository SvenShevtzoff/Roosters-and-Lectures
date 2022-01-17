from re import L
import pandas as pd
from classes.activities import Activity
from classes.roomslots import Roomslot


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
        return [x for x in self._roomslots.get_list() if room == x.get_room().get_roomnumber() and x.get_activity() is not None]

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

    def get_conflicts_student(self, student):
        dictionary = {}
        for x in self._activities.get_list():
            student_names = [i.get_name() for i in x.get_students()]
            if student in student_names:
                if f"{x.get_roomslot().get_day()}, {x.get_roomslot().get_time()}" in dictionary:
                    dictionary[f"{x.get_roomslot().get_day()}, {x.get_roomslot().get_time()}"].append(x.get_roomslot())
                else:
                    dictionary[f"{x.get_roomslot().get_day()}, {x.get_roomslot().get_time()}"] = [x.get_roomslot()]

        return [x for x in dictionary.values() if len(x) > 1]
    
    def get_conflicts_course(self, course_name):
        dictionary = {}
        course_activities = []
        for activity in self._activities.get_list():
            if activity.get_course().__str__() == course_name:
                course_activities = activity.get_course().get_activities()
                for activity in course_activities:
                    print(activity)
                break
        
        for activity in course_activities:
            if f"{activity.get_roomslot().get_day()}, {activity.get_roomslot().get_time()}" in dictionary:
                dictionary[f"{activity.get_roomslot().get_day()}, {activity.get_roomslot().get_time()}"].append(activity.get_roomslot())
            else:
                dictionary[f"{activity.get_roomslot().get_day()}, {activity.get_roomslot().get_time()}"] = [activity.get_roomslot()]
        
        return [x for x in dictionary.values() if len(x) > 1]
    
    
    def print_activities(self):
        print("schedule.py")
        for activity in self._activities.get_list():
            print(activity)


    def fitness(self):
        df_to_test = self.to_df()
        malus_points = self.max_roomsize_check()
        malus_points += self.use_17_slot_check()
        malus_points += self.course_conflict_check()
        malus_points += self.empty_roomslot_check(df_to_test)

        return malus_points

    def to_df(self):
        schedule = pd.DataFrame(columns=["day", "time", "room", "activity", "students"])
        for slot in self._roomslots.get_list():
            if not slot.get_activity():
                schedule = schedule.append({
                    "day": slot.get_day(),
                    "time": slot.get_time(),
                    "room": slot.get_room(),
                    "activity": None,
                    "students": None},
                    ignore_index=True)
            else:
                students = []
                for student in slot.get_course().get_students():
                    students.append(student.__str__())
                schedule = schedule.append({
                    "day": slot.get_day(),
                    "time": slot.get_time(),
                    "room": slot.get_room(),
                    "activity": slot.get_activity(),
                    "students": students},
                    ignore_index=True)

        return schedule

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
        num_of_times_17_slot_used = 0
        for slot in self.get_roomslots().get_list():
            if slot.get_time() == 17 and slot.get_activity():
                num_of_times_17_slot_used += 1
        malus_points += 5 * num_of_times_17_slot_used

        return malus_points

    def course_conflict_check(self):
        '''vakconflicten (1)'''
        malus_points = 0
        for student in self.get_students().get_list():
            student_name = student.get_name()
            num_of_conflicts = len(self.get_conflicts_student(student_name))
            malus_points += num_of_conflicts
        # schedule_exploded = df_to_test.explode("students")
        # # in de regel hieronder gaat iets fout ik weet niet wat
        # schedule_conflicts = schedule_exploded[["students", "day", "time", "activity"]].groupby(["students", "day", "time"]).count()
        # for i in schedule_conflicts.index:
        #     if schedule_conflicts["activity"][i] > 1:
        #         malus_points += (schedule_conflicts["activity"][i] - 1)

        return malus_points

    def empty_roomslot_check(self, df_to_test):
        '''één tussenslot (1) of twee tussensloten (3)'''
        malus_points = 0
        for student in self.get_students().get_list():
            # dit klopt straks niet meer
            students_activities = student.get_activities()
            # dummy activity
            previous_activity = Activity("dummy_kind", "dummy_course")
            previous_activity.set_roomslot(Roomslot("dummy_day", "dummy_time", "dummy_room"))
            for activity in students_activities:
                current_day = activity.get_roomslot().get_day()
                current_time = activity.get_roomslot().get_time()
                previous_day = previous_activity.get_roomslot().get_day()
                previous_time = previous_activity.get_roomslot().get_time()
                if current_day == previous_day:
                    if abs(current_time - previous_time) == 4:
                        malus_points += 1
                    if abs(current_time - previous_time) == 6:
                        malus_points += 3
                previous_activity = activity

        # malus_points = 0
        # previous_student = ("dummy_name", "dummy_day", "dummy_time")
        # schedule_exploded = df_to_test.explode("students")
        # schedule_conflicts = schedule_exploded[["students", "day", "time", "activity"]].groupby(["students", "day", "time"]).count()
        # for row in schedule_conflicts.index:
        #     if row[0:2] == previous_student[0:2]:
        #         if abs(row[2] - previous_student[2]) == 4:
        #             malus_points += 1
        #         if abs(row[2] - previous_student[2]) == 6:
        #             malus_points += 3
        #     previous_student = row

        return malus_points
