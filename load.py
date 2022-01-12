from classes import Room, Roomslot, Activity, Student, Course
import csv, sys, math

times = [9, 11, 13, 15]
days = ["ma", "di", "wo", "do", "vr"]


def load(file_name_rooms, file_name_courses, file_name_students):
    """ Function to load in all needed data """
    try:
        file_rooms = open(file_name_rooms, 'r')
        file_courses = open(file_name_courses, 'r')
        file_students = open(file_name_students, 'r')
    except OSError:
        print("Could not open/read file(s)")
        sys.exit()

    # loading rooms
    rooms = []
    with file_rooms:
        csv_reader = csv.reader(file_rooms, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            rooms.append(Room(row[0], int(row[1])))

    # loading courses
    activities = []
    courses = []
    with file_courses:
        csv_reader = csv.reader(file_courses, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            # creating Lecture, Tutorial and Practicum objects
            course_name = row[0]
            courses.append(Course(course_name))
            for i in range(int(row[1])):
                activities.append(Activity("Lecture", course_name, int(row[6])))
            if row[3] != "nvt":
                for i in range(int(row[2]) * math.ceil(int(row[6]) / int(row[3]))):
                    activities.append(Activity("Tutorial", course_name, int(row[3])))
            if row[5] != "nvt":
                for i in range(int(row[4]) * math.ceil(int(row[6]) / int(row[5]))):
                    activities.append(Activity("Practicum", course_name, int(row[5])))

    # creating Roomslot objects
    roomslots = []
    for day in days:
        for time in times:
            for room in rooms:
                roomslots.append(Roomslot(day, time, room))

    # creating Student objects
    students = []
    with file_students:
        csv_reader = csv.reader(file_students, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            for i in range(3, 8):
                if row[i]:
                    for course in courses:
                        if course.get_name() == row[i]:
                            course.add_student()
                else:
                    break
            students.append(Student(row[0], row[1], row[2], courses))
    
    for course in courses:
        print(course)

    return courses, activities, roomslots, students

courses, activities, roomslots, students = load("data/rooms.csv", "data/courses.csv", "data/students_and_courses.csv")
