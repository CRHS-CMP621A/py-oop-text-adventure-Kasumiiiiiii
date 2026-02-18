# task 1
class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
# task 3
        self.linked_rooms = {}
# challenge 5
        self.items = {}
# character task 5
        self.character = None

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

# challenge 5
    def add_item(self, item_obj):
        self.items[item_obj.get_name()] = item_obj
        print(f"{item_obj.get_name()} added to {self.name}!")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from {self.name}!")
        else:
            print(f"{item_name} not found in {self.name}!")

# task 4
    def get_details(self):
        print(self.name)
        print("======================")
        print(self.description)
        # challenge 5
        if self.items:
            print("Items in this room: ")
            for item_name in self.items:
                item = self.items[item_name]
                print(f"> {item_name}: {item.description}")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

# task 5
#     def move(self, direction):
#         if direction in self.linked_rooms:
#             return self.linked_rooms[direction]
#         else:
#             print("You can't go that way")
#             return self
        
# challenge 5
    def move(self, command):
        if command in self.linked_rooms:
            return self.linked_rooms[command]
        elif command in self.items:
            item = self.items[command]
            if item.is_pickable:
                print(f"you picked up the {command}!")
                self.remove_item(command)
            else:
                print(f"You can't pick up the {command}! It's not pickable!")
            return self
        else:
            print("You can't go that way and no such item to pick up!")
            return self
        
# character task 7
    def set_character(self, char_obj):
        self.character = char_obj

    def get_character(self):
        return self.character
