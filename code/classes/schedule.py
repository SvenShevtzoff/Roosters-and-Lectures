import pandas as pd
from collections import Counter

class Schedule:

    def __init__(self, roomslots, activities):
        self._roomslots = roomslots
        self._activities = activities

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

    def check_conflict(self, student):
        dictionary = dict()
        for x in self._activities.get_list():
            student_names = [i.get_name() for i in x.get_students()]
            if student in student_names:
                if f"{x.get_roomslot().get_day()}, {x.get_roomslot().get_time()}" in dictionary:
                    dictionary[f"{x.get_roomslot().get_day()}, {x.get_roomslot().get_time()}"].append(x.get_roomslot())
                else :
                    dictionary[f"{x.get_roomslot().get_day()}, {x.get_roomslot().get_time()}"] = [x.get_roomslot()]
                    
        return [x for x in dictionary.values() if len(x) > 1]
        

        
    
    def fitness(self):
        df_to_test = self.to_df()
        malus_points = self.max_roomsize_check(df_to_test)
        malus_points += self.use_17_slot_check(df_to_test)
        malus_points += self.course_conflict_check(df_to_test)
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
    
    def max_roomsize_check(self, df_to_test):
        '''aantal studenten groter dan maximum toegestaan in de zaal (1)'''
        malus_points = 0
        for i in df_to_test.index:
            if df_to_test["activity"][i]:
                number_of_students = len(df_to_test["students"][i])
                room_capacity = df_to_test["room"][i].get_capacity()
                difference = number_of_students - room_capacity
                if difference > 0:
                    malus_points += difference
        
        return malus_points

    def use_17_slot_check(self, df_to_test):
        '''gebruik van avondslot (5)'''
        malus_points = 0
        schedule_evening = df_to_test.loc[(df_to_test["time"] == 17) & df_to_test["activity"]]
        malus_points += 5 * len(schedule_evening.index)

        return malus_points

    def course_conflict_check(self, df_to_test):
        '''vakconflicten (1)'''
        malus_points = 0
        schedule_exploded = df_to_test.explode("students")
        # in de regel hieronder gaat iets fout ik weet niet wat
        schedule_conflicts = schedule_exploded[["students", "day", "time", "activity"]].groupby(["students", "day", "time"]).count()
        for i in schedule_conflicts.index:
            if schedule_conflicts["activity"][i] > 1:
                malus_points += (schedule_conflicts["activity"][i] - 1)

        return malus_points

    def empty_roomslot_check(self, df_to_test):
        '''één tussenslot (1) of twee tussensloten (3)'''
        malus_points = 0
        previous_student = ("dummy_name", "dummy_day", "dummy_time")
        schedule_exploded = df_to_test.explode("students")
        schedule_conflicts = schedule_exploded[["students", "day", "time", "activity"]].groupby(["students", "day", "time"]).count()
        for row in schedule_conflicts.index:
            if row[0:2] == previous_student[0:2]:
                if abs(row[2] - previous_student[2]) == 4:
                    malus_points += 1
                if abs(row[2] - previous_student[2]) == 6:
                    malus_points += 3
            previous_student = row

        return malus_points

