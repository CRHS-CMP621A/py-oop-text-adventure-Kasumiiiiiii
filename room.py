# task 1
class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
# task 3
        self.linked_rooms = {}

# task 2
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

# task 3
    def get_name(self):
        return self.name
    
    def set_name(self, room_name):
        self.name = room_name
    
    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        print(self.name + " linked rooms: " + repr(self.linked_rooms))

# task 4
    def get_details(self):
        print(self.name)
        print("======================")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

# task 5
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self