from code.classes.rooms import Room, Rooms
from code.classes.courses import Course, Courses
from code.classes.roomslots import Roomslot, Roomslots
from code.classes.activities import Activity, Activities
from code.classes.students import Student, Students
import csv
import sys
from code.classes.schedule import *

times = [9, 11, 13, 15, 17]
days = ["Mon", "Thu", "Wed", "Thu", "Fri"]


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
    rooms = {}
    with file_rooms:
        csv_reader = csv.reader(file_rooms, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            rooms[row[0]] = Room(row[0], int(row[1]))

    # creating Rooms object
    rooms = Rooms(rooms)

    # loading courses
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
            num_of_lectures = int(row[1])
            new_course = Course(course_name, num_of_lectures)
            courses[course_name] = new_course

            # create Lecture, Tutorial and Practicum Activity objects
            for i in range(int(row[1])):
                new_activity = Activity("Lecture", new_course, int(row[6]))
                activities[f"Lecture {course_name}"] = new_activity
                courses[course_name].add_activity(new_activity)
            if row[3] != "nvt":
                for i in range(num_of_tutorials):
                    new_activity = Activity("Tutorial", new_course, int(row[3]))
                    activities[f"Tutorial {course_name}"] = new_activity
                    courses[course_name].add_activity(new_activity)
            if row[5] != "nvt":
                for i in range(num_of_practica):
                    new_activity = Activity("Practicum", new_course, int(row[5]))
                    activities[f"Practicum {course_name}"] = new_activity
                    courses[course_name].add_activity(new_activity)

    # creating activities and courses objects
    activities = Activities(activities)
    courses = Courses(courses)

    # creating Roomslot objects
    roomslots = {}
    for day in days:
        for room in rooms.get_list():
            if room.get_roomnumber() != "C0.110":
                times2 = times[0:4]
            else:
                times2 = times
            for time in times2:
                roomslots[f"Day: {day}, time: {time}, room: {room}"] = Roomslot(day, time, room)

    # creating Roomslots object
    roomslots = Roomslots(roomslots)

    # creating Student objects
    students = {}
    with file_students:
        csv_reader = csv.reader(file_students, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            students_courses = []
            for i in range(3, 8):
                if row[i]:
                    students_courses.append(courses.get_single(row[i]))
                else:
                    break
            new_student = Student(row[0], row[1], row[2], students_courses)
            students[row[2]] = new_student

            for course in students_courses:
                course.add_student(new_student)

    # creating Students object
    students = Students(students)

    # for each course, add students to its currently existing activities
    courses.add_students_to_activities()

    return courses, activities, roomslots, students
