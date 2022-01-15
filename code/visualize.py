'''Visualizing the schedule'''
import matplotlib.pyplot as plt

def visualize_non_student(roomslot_list):
    plot = plot_setup()
    for slot in roomslot_list:
        # getting the kind of the activity in the roomslot to set the element_color
        if slot.get_activity().get_kind() == 'Lecture':
            element_color = "blue"
        elif slot.get_activity().get_kind() == 'Tutorial':
            element_color = "red"
        elif slot.get_activity().get_kind() == 'Practicum':
            element_color = "orange"
        
        # calculating x and y coordinates according to day and time
        day_to_xcoord = {
            "Mon": 0,
            "Tue": 40,
            "Wed": 80,
            "Thu": 120,
            "Fri": 160
        }
        time_to_ycoord = {
            9: 40,
            11: 30,
            13: 20,
            15: 10,
            17: 0
        }
        xcoord = day_to_xcoord[slot.get_day()]
        ycoord = time_to_ycoord[slot.get_time()]

        # plotting the element and annotating it
        plot.broken_barh([(xcoord, 40)], (ycoord, 10), facecolors =(f'tab:{element_color}'))
        plot.annotate(f"{slot.get_activity().get_kind()} {slot.get_room()}", (xcoord + 1, ycoord + 8))

        # if course name to long put on two lines
        if len(slot.get_course().__str__()) < 25:
            plot.annotate(slot.get_course(), (xcoord + 1, ycoord + 6))
        else:
            plot.annotate(slot.get_course().__str__()[0:26], (xcoord + 1, ycoord + 6))
            plot.annotate(slot.get_course().__str__()[26:], (xcoord + 1, ycoord + 4))

    
    # plot
    plot.grid(True)
    plt.savefig("../doc/schedule.png")


def visualize_student(roomslot_list):
    plot = plot_setup
    for slot in roomslot_list:
        # getting the kind of the activity in the roomslot to set the element_color
        if slot.get_activity().get_kind() == 'Lecture':
            element_color = "blue"
        elif slot.get_activity().get_kind() == 'Tutorial':
            element_color = "red"
        elif slot.get_activity().get_kind() == 'Practicum':
            element_color = "orange"
        
        # calculating x and y coordinates according to day and time
        day_to_xcoord = {
            "Mon": 0,
            "Tue": 40,
            "Wed": 80,
            "Thu": 120,
            "Fri": 160
        }
        time_to_ycoord = {
            9: 40,
            11: 30,
            13: 20,
            15: 10,
            17: 0
        }
        xcoord = day_to_xcoord[slot.get_day()]
        ycoord = time_to_ycoord[slot.get_time()]

        # plotting the element and annotating it
        plot.broken_barh([(xcoord, 40)], (ycoord, 10), facecolors =(f'tab:{element_color}'))
        plot.annotate(f"{slot.get_activity().get_kind()} {slot.get_room()}", (xcoord + 1, ycoord + 8))

        # if course name to long put on two lines
        if len(slot.get_course().__str__()) < 25:
            plot.annotate(slot.get_course(), (xcoord + 1, ycoord + 6))
        else:
            plot.annotate(slot.get_course().__str__()[0:26], (xcoord + 1, ycoord + 6))
            plot.annotate(slot.get_course().__str__()[26:], (xcoord + 1, ycoord + 4))

    
    # plot
    plot.grid(True)
    plt.savefig("../doc/schedule.png")


def plot_setup():
    # setting up plot
    plt.rcParams["figure.figsize"] = (15, 7.5)
    fig, gnt = plt.subplots()

    gnt.set_ylabel('hours')
    gnt.set_ylim(0, 50)
    gnt.set_yticks([0, 10, 20, 30, 40, 50])
    gnt.set_yticklabels(['19', '17', '15', '13', '11', '9'])

    gnt.set_xlabel('days')
    gnt.set_xlim(0,200)
    gnt.set_xticks([0, 40, 80, 120, 160])
    gnt.set_xticklabels(["Mon", "Thu", "Wed", "Thu", "Fri"], ha='left')

    return gnt
