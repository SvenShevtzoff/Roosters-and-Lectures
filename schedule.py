import pandas as pd
class Schedule:

    def __init__(self, roomslots, activities):
        self._roomslots = roomslots
        self._activities = activities

    def course_schedule(self, course):
        return [x.get_roomslot() for x in self._activities.get_list() if course == x.get_course().get_name()]
    
    def room_schedule(self, room):
        return [x for x in self._roomslots.get_list() if room == x.get_room().get_roomnumber()]

    def student_schedule(self, student):
        #niet zeker of deze werkt
        schedule = []
        for x in self._activities.get_list():
            student_names = [i.get_name() for i in x.get_students()]
            if student in student_names:
                schedule.append(x.get_roomslot())
        return schedule

    def day_schedule(self, day):
        return [x for x in self._roomslots.get_list() if day == x.get_day()]

    def time_schedule(self, time):
        return [x for x in self._roomslots.get_list() if time == x.get_time()]

    # als we dit zo willen doen is de file fitness niet meer nofig 
    def fitness(self):
        df = pd.DataFrame(columns=["day", "time", "room", "activity"])
        for slot in self._roomslots.get_list():
            if not slot.get_activity():
                schedule = df.append({
                    "day": slot.get_day(),
                    "time": slot.get_time(),
                    "room": slot.get_room(),
                    "activity": None,
                    "students": None}, 
                    ignore_index=True)
            else:
                students = []
                for student in slot.get_course().get_students():
                    students.append(student)
                df = df.append({
                    "day": slot.get_day(),
                    "time": slot.get_time(),
                    "room": slot.get_room(),
                    "activity": slot.get_activity(),
                    "students": students}, 
                    ignore_index=True)
        
        malus_points = 0

        # aantal studenten groter dan maximum toegestaan in de zaal (1)
        for i in schedule.index:
            if schedule["activity"][i]:
                number_of_students = len(schedule["students"][i])
                room_capacity = schedule["room"][i].get_capacity()
                difference = number_of_students - room_capacity
                if difference > 0:
                    malus_points += difference

        # gebruik van avondslot (5)
        schedule_evening = schedule.loc[(schedule["time"] == 17) & schedule["activity"]]
        malus_points += 5 * len(schedule_evening.index)

        # vakconflicten (1)
        schedule_exploded = schedule.explode("students")
        #in de regel hieronder gaat iets fout ik weet niet wat
        schedule_conflicts = schedule_exploded[["students", "day", "time", "activity"]].groupby(["students", "day", "time"]).count()

        for i in schedule_conflicts.index:
            if schedule_conflicts["activity"][i] > 1:
                malus_points += (schedule_conflicts["activity"][i] - 1)
        schedule_conflicts.to_csv("students.csv")

        # één tussenslot (1) of twee tussensloten (3)
        previous_student = ("dummy_name", "dummy_day", "dummy_time")
        for row in schedule_conflicts.index:
            if row[0:2] == previous_student[0:2]:
                if abs(row[2] - previous_student[2]) == 4:
                    malus_points += 1
                if abs(row[2] - previous_student[2]) == 6:
                    malus_points += 3
            previous_student = row

        return malus_points
