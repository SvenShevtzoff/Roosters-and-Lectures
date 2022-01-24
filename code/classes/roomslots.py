# =============================================================================
# roomslots.py with classes roomslot and roomslots
# =============================================================================

class Roomslot:

    def __init__(self, day, time, room, activity=None):
        self._day = day
        self._time = time
        self._room = room
        self._activity = activity
        self._visualized = False

    def day(self):
        """Returns the day of the roomslot"""
        return self._day

    def time(self):
        """Returns the time of the roomslot"""
        return self._time

    def room(self):
        """Returns the room object of the roomslot"""
        return self._room

    def activity(self):
        """Returns the activity object connected to the roomslot"""
        return self._activity

    def course(self):
        """Returns the course object connected to the activity object of the roomslot"""
        return self._activity.course()

    def set_activity(self, activity):
        """Connects an activity object to the roomslot object"""
        self._activity = activity

    def remove_activity(self):
        self._activity = None

    def is_visualized(self):
        return self._visualized

    def set_visualized(self):
        self._visualized = True

    def __str__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"

    def __repr__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"


class Roomslots:

    def __init__(self, roomslots):
        self._roomslots_dict = roomslots

    def dict(self):
        """Returns a dictionary of the roomslots"""
        return self._roomslots_dict

    def list(self):
        """Returns a list of the roomslots"""
        self._roomslots_list = []
        for slot in list(self._roomslots_dict.values()):
            self._roomslots_list.append(slot)
        return self._roomslots_list
