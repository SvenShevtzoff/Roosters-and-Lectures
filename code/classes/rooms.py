class Room:

    def __init__(self, roomnumber, capacity):
        self._roomnumber = roomnumber
        self._capacity = capacity

    def get_roomnumber(self):
        return self._roomnumber

    def get_capacity(self):
        return self._capacity

    def __str__(self):
        return self._roomnumber


class Rooms:

    def __init__(self, rooms):
        self._rooms_dict = rooms

    def get_dict(self):
        return self._rooms_dict

    def get_list(self):
        self._rooms_list = []
        for room in list(self._rooms_dict.values()):
            self._rooms_list.append(room)
        return self._rooms_list
