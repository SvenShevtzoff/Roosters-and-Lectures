from classes import Room, Roomslot, Activity
import csv, sys

times = [9, 11, 13, 15]
days = ["ma", "di", "wo", "do", "vr"]


def load(file_name_rooms, file_name_courses):
    """ Function to load in all needed data """
    try:
        file_rooms = open(file_name_rooms, 'r')
        file_courses = open(file_name_courses, 'r')
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
    with file_courses:
        csv_reader = csv.reader(file_courses, delimiter=";")
        next(csv_reader)
        for row in csv_reader:
            # creating Lecture, Tutorial and Practicum objects
            course_name = row[0]
            for i in range(int(row[1])):
                activities.append(Activity("Lecture", course_name, int(row[6])))
            for i in range(int(row[2])):
                activities.append(Activity("Tutorial", course_name, int(row[3])))
            for i in range(int(row[4])):
                activities.append(Activity("Practicum", course_name, int(row[5])))

    # creating Roomslot objects
    unique_id = 0
    roomslots = []
    for day in days:
        for time in times:
            for room in rooms:
                roomslots.append(Roomslot(unique_id, day, time, room))
                unique_id += 1

    return activities, roomslots
