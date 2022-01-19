'''Visualizing the schedule'''
import matplotlib.pyplot as plt

# defining dictionaries to calculate the coordinates from day/time
day_to_xcoord = {
    "Mon": 0,
    "Tue": 40,
    "Wed": 80,
    "Thu": 120,
    "Fri": 160}
time_to_ycoord = {
    9: 40,
    11: 30,
    13: 20,
    15: 10,
    17: 0}


def visualize_room(schedule, room):
    plot = plot_setup()

    schedule = schedule.room_schedule(room)

    for slot in schedule:
        # calculating x and y coordinates according to day and time
        xcoord = day_to_xcoord[slot.get_day()] + 2
        ycoord = time_to_ycoord[slot.get_time()] + 1

        # plotting the element and annotating it
        plot.broken_barh([(xcoord, 36)], (ycoord, 8), facecolors=(f'tab:{get_element_color(slot)}'))
        plot.annotate(f"{slot.get_activity().get_kind()} {slot.get_room()}", (xcoord + 1, ycoord + 6))

        # if course name to long put on two lines
        if len(str(slot.get_course())) < 20:
            plot.annotate(slot.get_course(), (xcoord + 1, ycoord + 4))
        else:
            plot.annotate(str(slot.get_course())[0:21], (xcoord + 1, ycoord + 4))
            plot.annotate(str(slot.get_course())[21:], (xcoord + 1, ycoord + 2))

    # plot
    plot.grid(True)
    return plot


def visualize_course(schedule, course):
    '''Visualizing the schedule for one student'''
    plot = plot_setup()

    # plotting all activity conflicts
    conflicts_list = schedule.get_conflicts_course(course)

    for conflicts in conflicts_list:
        # drawing red box around conflict
        xcoord = day_to_xcoord[conflicts[0].get_day()]
        ycoord = time_to_ycoord[conflicts[0].get_time()]
        plot.broken_barh([(xcoord, 40)], (ycoord, 10), facecolors=('tab:red'))
        if len(conflicts) == 2:
            # plot left activity
            plot.broken_barh([(xcoord + 2, 18)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[0])}'))
            plot.annotate(conflicts[0].get_room(), (xcoord + 3, ycoord + 7))
            plot.annotate(str(conflicts[0].get_course())[:12], (xcoord + 3, ycoord + 5))
            plot.annotate(str(conflicts[0].get_course())[11:24], (xcoord + 3, ycoord + 3))
            # plot right activity
            plot.broken_barh([(xcoord + 20, 18)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[1])}'))
            plot.annotate(conflicts[1].get_room(), (xcoord + 21, ycoord + 7))
            plot.annotate(str(conflicts[1].get_course())[:12], (xcoord + 21, ycoord + 5))
            plot.annotate(str(conflicts[1].get_course())[11:24], (xcoord + 21, ycoord + 3))

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()
        elif len(conflicts) == 3:
            # plot left activity
            plot.broken_barh([(xcoord + 2, 12)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[0])}'))
            plot.annotate(conflicts[0].get_room(), (xcoord + 3, ycoord + 7))
            plot.annotate(str(conflicts[0].get_course())[:8], (xcoord + 3, ycoord + 5))
            plot.annotate(str(conflicts[0].get_course())[7:15], (xcoord + 3, ycoord + 3))
            # plot middle activity
            plot.broken_barh([(xcoord + 14, 12)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[1])}'))
            plot.annotate(conflicts[1].get_room(), (xcoord + 15, ycoord + 7))
            plot.annotate(str(conflicts[1].get_course())[:8], (xcoord + 15, ycoord + 5))
            plot.annotate(str(conflicts[1].get_course())[7:15], (xcoord + 15, ycoord + 3))
            # plot right activity
            plot.broken_barh([(xcoord + 26, 12)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[2])}'))
            plot.annotate(conflicts[2].get_room(), (xcoord + 27, ycoord + 7))
            plot.annotate(str(conflicts[2].get_course())[:8], (xcoord + 27, ycoord + 5))
            plot.annotate(str(conflicts[2].get_course())[7:15], (xcoord + 27, ycoord + 3))

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()
        elif len(conflicts) == 4:
            # plot left top activity
            plot.broken_barh([(xcoord + 2, 18)], (ycoord + 1, 4), facecolors=(f'tab:{get_element_color(conflicts[0])}'))
            plot.annotate(conflicts[0].get_room(), (xcoord + 3, ycoord + 7))
            # plot left bottom activity
            plot.broken_barh([(xcoord + 2, 18)], (ycoord + 1, 4), facecolors=(f'tab:{get_element_color(conflicts[0])}'))
            plot.annotate(conflicts[1].get_room(), (xcoord + 3, ycoord + 3))
            # plot right `top activity
            plot.broken_barh([(xcoord + 20, 18)], (ycoord + 5, 4), facecolors=(f'tab:{get_element_color(conflicts[1])}'))
            plot.annotate(conflicts[2].get_room(), (xcoord + 21, ycoord + 7))
            plot.annotate(str(conflicts[2].get_course())[:13], (xcoord + 21, ycoord + 5))
            plot.annotate(str(conflicts[2].get_course())[12:25], (xcoord + 21, ycoord + 3))
            # plot right bottom activity
            plot.broken_barh([(xcoord + 20, 18)], (ycoord + 5, 4), facecolors=(f'tab:{get_element_color(conflicts[1])}'))
            plot.annotate(conflicts[3].get_room(), (xcoord + 21, ycoord + 3))
            plot.annotate(str(conflicts[3].get_course())[:13], (xcoord + 21, ycoord + 5))
            plot.annotate(str(conflicts[3].get_course())[12:25], (xcoord + 21, ycoord + 3))

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()

    # printing the rest of the activities
    student_schedule = schedule.course_schedule(course)
    for slot in student_schedule:
        if not slot.is_visualized():
            # calculating x and y coordinates according to day and time
            xcoord = day_to_xcoord[slot.get_day()] + 2
            ycoord = time_to_ycoord[slot.get_time()] + 1

            # plotting the element and annotating it
            plot.broken_barh([(xcoord, 36)], (ycoord, 8), facecolors=(f'tab:{get_element_color(slot)}'))
            plot.annotate(f"{slot.get_activity().get_kind()} {slot.get_room()}", (xcoord + 1, ycoord + 6))

            # if course name to long spread over two lines
            if len(str(slot.get_course())) < 20:
                plot.annotate(slot.get_course(), (xcoord + 1, ycoord + 4))
            else:
                plot.annotate(str(slot.get_course())[0:21], (xcoord + 1, ycoord + 4))
                plot.annotate(str(slot.get_course())[21:], (xcoord + 1, ycoord + 2))

    # plot
    plot.grid(True)
    return plot


def visualize_student(schedule, student):
    '''Visualizing the schedule for one student'''
    plot = plot_setup()

    # plotting all activity conflicts
    conflicts_list = schedule.get_conflicts_student(student)

    for conflicts in conflicts_list:
        # drawing red box around conflict
        xcoord = day_to_xcoord[conflicts[0].get_day()]
        ycoord = time_to_ycoord[conflicts[0].get_time()]
        plot.broken_barh([(xcoord, 40)], (ycoord, 10), facecolors=('tab:red'))
        if len(conflicts) == 2:
            # plot left activity
            plot.broken_barh([(xcoord + 2, 18)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[0])}'))
            plot.annotate(conflicts[0].get_room(), (xcoord + 3, ycoord + 7))
            plot.annotate(str(conflicts[0].get_course())[:12], (xcoord + 3, ycoord + 5))
            plot.annotate(str(conflicts[0].get_course())[11:24], (xcoord + 3, ycoord + 3))
            # plot right activity
            plot.broken_barh([(xcoord + 20, 18)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[1])}'))
            plot.annotate(conflicts[1].get_room(), (xcoord + 21, ycoord + 7))
            plot.annotate(str(conflicts[1].get_course())[:12], (xcoord + 21, ycoord + 5))
            plot.annotate(str(conflicts[1].get_course())[11:24], (xcoord + 21, ycoord + 3))

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()
        elif len(conflicts) == 3:
            # plot left activity
            plot.broken_barh([(xcoord + 2, 12)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[0])}'))
            plot.annotate(conflicts[0].get_room(), (xcoord + 3, ycoord + 7))
            plot.annotate(str(conflicts[0].get_course())[:8], (xcoord + 3, ycoord + 5))
            plot.annotate(str(conflicts[0].get_course())[7:15], (xcoord + 3, ycoord + 3))
            # plot middle activity
            plot.broken_barh([(xcoord + 14, 12)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[1])}'))
            plot.annotate(conflicts[1].get_room(), (xcoord + 15, ycoord + 7))
            plot.annotate(str(conflicts[1].get_course())[:8], (xcoord + 15, ycoord + 5))
            plot.annotate(str(conflicts[1].get_course())[7:15], (xcoord + 15, ycoord + 3))
            # plot right activity
            plot.broken_barh([(xcoord + 26, 12)], (ycoord + 1, 8), facecolors=(f'tab:{get_element_color(conflicts[2])}'))
            plot.annotate(conflicts[2].get_room(), (xcoord + 27, ycoord + 7))
            plot.annotate(str(conflicts[2].get_course())[:8], (xcoord + 27, ycoord + 5))
            plot.annotate(str(conflicts[2].get_course())[7:15], (xcoord + 27, ycoord + 3))

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()
        elif len(conflicts) == 4:
            # plot left top activity
            plot.broken_barh([(xcoord + 2, 18)], (ycoord + 1, 4), facecolors=(f'tab:{get_element_color(conflicts[0])}'))
            plot.annotate(conflicts[0].get_room(), (xcoord + 3, ycoord + 7))
            # plot left bottom activity
            plot.broken_barh([(xcoord + 2, 18)], (ycoord + 1, 4), facecolors=(f'tab:{get_element_color(conflicts[0])}'))
            plot.annotate(conflicts[1].get_room(), (xcoord + 3, ycoord + 3))
            # plot right `top activity
            plot.broken_barh([(xcoord + 20, 18)], (ycoord + 5, 4), facecolors=(f'tab:{get_element_color(conflicts[1])}'))
            plot.annotate(conflicts[2].get_room(), (xcoord + 21, ycoord + 7))
            plot.annotate(str(conflicts[2].get_course())[:13], (xcoord + 21, ycoord + 5))
            plot.annotate(str(conflicts[2].get_course())[12:25], (xcoord + 21, ycoord + 3))
            # plot right bottom activity
            plot.broken_barh([(xcoord + 20, 18)], (ycoord + 5, 4), facecolors=(f'tab:{get_element_color(conflicts[1])}'))
            plot.annotate(conflicts[3].get_room(), (xcoord + 21, ycoord + 3))
            plot.annotate(str(conflicts[3].get_course())[:13], (xcoord + 21, ycoord + 5))
            plot.annotate(str(conflicts[3].get_course())[12:25], (xcoord + 21, ycoord + 3))

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()

    # printing the rest of the activities
    student_schedule = schedule.student_schedule(student.get_name())
    for slot in student_schedule:
        if not slot.is_visualized():
            # calculating x and y coordinates according to day and time
            xcoord = day_to_xcoord[slot.get_day()] + 2
            ycoord = time_to_ycoord[slot.get_time()] + 1

            # plotting the element and annotating it
            plot.broken_barh([(xcoord, 36)], (ycoord, 8), facecolors=(f'tab:{get_element_color(slot)}'))
            plot.annotate(f"{slot.get_activity().get_kind()} {slot.get_room()}", (xcoord + 1, ycoord + 6))

            # if course name to long spread over two lines
            if len(str(slot.get_course())) < 20:
                plot.annotate(slot.get_course(), (xcoord + 1, ycoord + 4))
            else:
                plot.annotate(str(slot.get_course())[0:21], (xcoord + 1, ycoord + 4))
                plot.annotate(str(slot.get_course())[21:], (xcoord + 1, ycoord + 2))

    # plot
    plot.grid(True)
    return plot


def plot_setup():
    '''Defining the starting settings for the schedule plot'''
    # setting up plot
    plt.rcParams["figure.figsize"] = (15, 7.5)
    fig, gnt = plt.subplots()

    # setting up y axis
    gnt.set_ylabel('hours')
    gnt.set_ylim(0, 50)
    gnt.set_yticks([0, 10, 20, 30, 40, 50])
    gnt.set_yticklabels(['19', '17', '15', '13', '11', '9'])

    # setting up x axis
    gnt.set_xlabel('days')
    gnt.set_xlim(0, 200)
    gnt.set_xticks([0, 40, 80, 120, 160])
    gnt.set_xticklabels(["Mon", "Thu", "Wed", "Thu", "Fri"], ha='left')

    return gnt


def get_element_color(slot):
    '''Getting the kind of the activity in the roomslot to set the element_color'''
    if slot.get_activity().get_kind() == 'Lecture':
        element_color = "blue"
    elif slot.get_activity().get_kind() == 'Tutorial':
        element_color = "pink"
    elif slot.get_activity().get_kind() == 'Practicum':
        element_color = "orange"

    return element_color
