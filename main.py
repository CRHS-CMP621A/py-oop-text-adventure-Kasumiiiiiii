# task 2
from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
kitchen.describe()

# task 3
dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with a long wooden table and chandeliers.")
dining_hall.describe()

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a polished wooden floor and a stage for music.")
ballroom.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

dining_hall.link_room(ballroom, "east")
ballroom.link_room(dining_hall, "west")

# task 4
dining_hall.get_details()
kitchen.get_details()
ballroom.get_details()