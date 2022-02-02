# =============================================================================
# visualize.py for visualizing the schedule
# =============================================================================
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
    """Visualizing the schedule for one room"""
    plot = plot_setup()
    schedule = schedule.room_schedule(room)

    for slot in schedule:
        # calculating x and y coordinates according to day and time
        xcoord = day_to_xcoord[slot.day()] + 2
        ycoord = time_to_ycoord[slot.time()] + 1

        # plot single activity
        plot_full(plot, xcoord, ycoord, slot)

    # plotting and saving plot
    plot.grid(True)
    plt.savefig(f"output/schedule_{str(room)}.png")


def visualize_course(schedule, course):
    """Visualizing the schedule for one course"""
    plot = plot_setup()

    # plotting all activity conflicts
    conflicts_list = schedule.conflicts_course(course)

    for conflicts in conflicts_list:
        # drawing red box around conflict
        xcoord = day_to_xcoord[conflicts[0].day()]
        ycoord = time_to_ycoord[conflicts[0].time()]
        plot.broken_barh([(xcoord, 40)], (ycoord, 10), facecolors=('tab:red'))

        if len(conflicts) == 2:
            # plot left activity
            plot_half(plot, xcoord, ycoord, conflicts[0])

            # plot right activity
            plot_half(plot, xcoord + 18, ycoord, conflicts[1])

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()
        elif len(conflicts) == 3:
            # plot left activity
            plot_half(plot, xcoord, ycoord, conflicts[0])
            # plot middle activity
            plot_half(plot, xcoord + 12, ycoord, conflicts[0])
            # plot right activity
            plot_half(plot, xcoord + 24, ycoord, conflicts[0])

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()
        elif len(conflicts) == 4:
            # plot left top activity
            plot.annotate("4 activities", (xcoord + 3, ycoord + 7))
            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()

    # printing the rest of the activities
    student_schedule = schedule.course_schedule(course)
    for slot in student_schedule:
        if not slot.is_visualized():
            # calculating x and y coordinates according to day and time
            xcoord = day_to_xcoord[slot.day()] + 2
            ycoord = time_to_ycoord[slot.time()] + 1

            # plot single activity
            plot_full(plot, xcoord, ycoord, slot)

    # plotting and saving plot
    plot.grid(True)
    plt.savefig(f"output/schedule_{course}.png")


def visualize_student(schedule, student_number):
    """Visualizing the schedule for one student, WARNING: make sure to enter student number"""
    plot = plot_setup()

    # plotting all activity conflicts
    conflicts_list = schedule.conflicts_student(student_number)

    for conflicts in conflicts_list:
        # drawing red box around conflict
        xcoord = day_to_xcoord[conflicts[0].day()]
        ycoord = time_to_ycoord[conflicts[0].time()]
        plot.broken_barh([(xcoord, 40)], (ycoord, 10), facecolors=('tab:red'))

        if len(conflicts) == 2:
            # plot left activity
            plot_half(plot, xcoord, ycoord, conflicts[0])

            # plot right activity
            plot_half(plot, xcoord + 18, ycoord, conflicts[1])

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()
        elif len(conflicts) == 3:
            # plot left activity
            plot_half(plot, xcoord, ycoord, conflicts[0])
            # plot middle activity
            plot_half(plot, xcoord + 12, ycoord, conflicts[0])
            # plot right activity
            plot_half(plot, xcoord + 24, ycoord, conflicts[0])

            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()
        elif len(conflicts) == 4:
            # plot left top activity
            plot.annotate("4 activities", (xcoord + 3, ycoord + 7))
            # setting the activity value to visualized, so it is not drawn twice
            for conflict in conflicts:
                conflict.set_visualized()

    # printing the rest of the activities
    student_schedule = schedule.student_schedule(student_number)
    for slot in student_schedule:
        if not slot.is_visualized():
            # calculating x and y coordinates according to day and time
            xcoord = day_to_xcoord[slot.day()] + 2
            ycoord = time_to_ycoord[slot.time()] + 1

            # plot single activity
            plot_full(plot, xcoord, ycoord, slot)

    # saving plot
    plot.grid(True)
    plt.savefig(f"output/schedule_{student_number}.png")


def plot_full(plot, xcoord, ycoord, slot):
    """Plot a full size block with an activity and annotate"""
    plot.broken_barh([(xcoord, 36)], (ycoord, 8), facecolors=(f'tab:{element_color(slot)}'))
    plot.annotate(f"{slot.activity().kind()} {slot.room()}", (xcoord + 1, ycoord + 6))

    # if course name to long put on two lines
    if len(str(slot.course())) < 20:
        plot.annotate(slot.course(), (xcoord + 1, ycoord + 4))
    else:
        plot.annotate(str(slot.course())[0:21], (xcoord + 1, ycoord + 4))
        plot.annotate(str(slot.course())[21:], (xcoord + 1, ycoord + 2))


def plot_half(plot, xcoord, ycoord, slot):
    """Plot a half size block with an activity and annotate"""
    plot.broken_barh([(xcoord + 2, 18)], (ycoord + 1, 8), facecolors=(f'tab:{element_color(slot)}'))
    plot.annotate(slot.room(), (xcoord + 3, ycoord + 7))
    plot.annotate(str(slot.course())[:12], (xcoord + 3, ycoord + 5))
    plot.annotate(str(slot.course())[11:24], (xcoord + 3, ycoord + 3))


def plot_third(plot, xcoord, ycoord, slot):
    """Plot a third size block with an activity and annotate"""
    plot.broken_barh([(xcoord + 2, 12)], (ycoord + 1, 8), facecolors=(f'tab:{element_color(slot)}'))
    plot.annotate(slot.room(), (xcoord + 3, ycoord + 7))
    plot.annotate(str(slot.course())[:8], (xcoord + 3, ycoord + 5))
    plot.annotate(str(slot.course())[7:15], (xcoord + 3, ycoord + 3))


def plot_setup():
    """Defining the starting settings for the schedule plot"""
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
    gnt.set_xticklabels(["Mon", "Tue", "Wed", "Thu", "Fri"], ha='left')

    return gnt


def element_color(slot):
    """Getting the kind of the activity in the roomslot to set the element_color"""
    if slot.activity().kind() == 'Lecture':
        element_color = "blue"
    elif slot.activity().kind() == 'Tutorial':
        element_color = "pink"
    elif slot.activity().kind() == 'Practicum':
        element_color = "orange"

    return element_color
