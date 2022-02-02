# =============================================================================
# load.py with fuctions to load all data from the given csv-files
# =============================================================================
from code.classes.rooms import Room, Rooms
from code.classes.courses import Course, Courses
from code.classes.roomslots import Roomslot, Roomslots
from code.classes.activities import Activity, Activities
from code.classes.students import Student, Students
import csv
import sys

TIMES = [9, 11, 13, 15, 17]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]


def load(file_name_rooms, file_name_courses, file_name_students):
    """ Function to load in all needed data """
    file_rooms, file_courses, file_students = load_open(file_name_rooms, file_name_courses, file_name_students)
    rooms = load_rooms(file_rooms)
    courses, activities = load_courses(file_courses)
    roomslots = load_roomslots(rooms)
    students = load_students(file_students, courses, activities)
    load_close(file_rooms, file_courses, file_students)
    return activities, roomslots, students, courses, rooms


def load_open(file_name_rooms, file_name_courses, file_name_students):
    """Opens the files, when unsuccesful exits"""
    try:
        file_rooms = open(file_name_rooms, 'r')
        file_courses = open(file_name_courses, 'r')
        file_students = open(file_name_students, 'r')
        return file_rooms, file_courses, file_students
    except OSError:
        print("Could not open/read file(s)")
        sys.exit()


def load_close(file_rooms, file_courses, file_students):
    """Closes the opened files"""
    file_rooms.close()
    file_courses.close()
    file_students.close()


def load_rooms(file_rooms):
    """Creating rooms from data"""
    rooms = {}
    with file_rooms:
        csv_reader = csv.reader(file_rooms, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            rooms[row[0]] = Room(row[0], int(row[1]))

    # creating Rooms object
    rooms = Rooms(rooms)
    return rooms


def load_courses(file_courses):
    """Creating courses from data"""
    activities = {}
    courses = {}
    with file_courses:
        csv_reader = csv.reader(file_courses, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            # creating Lecture, Tutorial and Practicum objects
            course_name = row[0]
            num_of_tutorials = int(row[2])
            num_of_practica = int(row[4])
            new_course = Course(course_name)
            courses[course_name] = new_course

            # create Lecture, Tutorial and Practicum Activity objects
            for i in range(int(row[1])):
                new_activity = Activity(str(i + 1), "Lecture", new_course, int(row[6]))
                activities[f"Lecture {course_name} {i + 1}"] = new_activity
                courses[course_name].add_activity(new_activity)
            if row[3] != "nvt":
                for i in range(num_of_tutorials):
                    new_activity = Activity(str(i + 1), "Tutorial", new_course, int(row[3]))
                    activities[f"Tutorial {course_name} {i + 1}"] = new_activity
                    courses[course_name].add_activity(new_activity)
            if row[5] != "nvt":
                for i in range(num_of_practica):
                    new_activity = Activity(str(i + 1), "Practicum", new_course, int(row[5]))
                    activities[f"Practicum {course_name} {i + 1}"] = new_activity
                    courses[course_name].add_activity(new_activity)

    # creating Activities and Courses objects
    activities = Activities(activities)
    courses = Courses(courses)

    return courses, activities


def load_roomslots(rooms):
    """Creating roomslots from rooms"""
    roomslots = {}
    for day in DAYS:
        for room in rooms.list():
            if room.roomnumber() != "C0.110":
                times_filtered = TIMES[0:4]
            else:
                times_filtered = TIMES
            for time in times_filtered:
                roomslots[f"{day} {time} {room}"] = Roomslot(day, time, room)

    # creating Roomslots object
    roomslots = Roomslots(roomslots)

    return roomslots


def load_students(file_students, courses, activities):
    """Creating students from data and adding to courses/activities"""
    students = {}
    with file_students:
        csv_reader = csv.reader(file_students, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            students_courses = []
            for i in range(3, 8):
                if row[i]:
                    students_courses.append(courses.single(row[i]))
                else:
                    break
            new_student = Student(row[0], row[1], row[2], students_courses)
            students[row[2]] = new_student

            for course in students_courses:
                course.add_student(new_student)

    # creating Students object
    students = Students(students)

    # for each course, add students to its currently existing activities
    courses.add_students_to_activities_per_course(activities, students)

    return students
