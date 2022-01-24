# =============================================================================
# roomslots.py with classes roomslot and roomslots
# =============================================================================

from calendar import c
import copy


class Roomslot:

    def __init__(self, day, time, room, activity=None):
        self._day = day
        self._time = time
        self._room = room
        self._activity = activity
        self._visualized = False

    def copy(self):
        new = copy.copy(self)
        new._day = copy.copy(self._day)
        new._time = copy.copy(self._time)
        new._room = copy.copy(self._room)
        new._activity = copy.copy(self._activity)
        new._visualized = False
        
        return new

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
        """Check if this roomslot has already been visualized"""
        return self._visualized

    def set_visualized(self):
        """Mark this roomslot as visualized"""
        self._visualized = True

    def __str__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"

    def __repr__(self):
        return f"Day: {self._day}, time: {self._time}, room: {self._room}, activity: {self._activity}"


class Roomslots:

    def __init__(self, roomslots):
        self._roomslots_dict = roomslots

    def list(self):
        """Returns a list of the roomslots"""
        return list(self._roomslots_dict.values())

    def copy(self):
        new = copy.copy(self)
        new._roomslots_dict = {}
        for slot in self.list():
            new._roomslots_dict[str(slot)] = slot.copy()
        return new
