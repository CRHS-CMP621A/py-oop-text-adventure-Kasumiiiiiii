# task 2
from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

# task 3
dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with a long wooden table and chandeliers.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a polished wooden floor and a stage for music.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "east")
ballroom.link_room(dining_hall, "west")

# task 5
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)