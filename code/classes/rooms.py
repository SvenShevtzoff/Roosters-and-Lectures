# =============================================================================
# rooms.py with classes room and rooms
# =============================================================================

class Room:

    def __init__(self, roomnumber, capacity):
        self._roomnumber = roomnumber
        self._capacity = capacity

    def roomnumber(self):
        """Returns roomnumber of a room object"""
        return self._roomnumber

    def capacity(self):
        """Returns the capacity of a room ovject"""
        return self._capacity

    def __str__(self):
        return self._roomnumber


class Rooms:

    def __init__(self, rooms):
        self._rooms_dict = rooms

    def list(self):
        """Returns a list of the rooms"""
        return list(self._rooms_dict.values())
