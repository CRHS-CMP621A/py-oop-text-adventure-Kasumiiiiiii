# task 2
from room import Room
# challenge 5
from item import Item
# character task 1
from character import Character

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dave = Character("Dave", "A smelly zombie")
dave.set_conversation()
dave.describe()

# task 3
dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with a long wooden table and chandeliers.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a polished wooden floor and a stage for music.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "east")
ballroom.link_room(dining_hall, "west")

# challenge 5
knife = Item("Knife")
knife.set_description("A sharp iron knife to fight enemies.")
knife.set_value(30)
kitchen.add_item(knife)

key = Item("Key")
key.set_description("A key to unlock the ballroom door.")
key.set_value(10)
dining_hall.add_item(key)

piano = Item("Piano")
piano.set_description("A grand piano that plays music.")
piano.is_pickable = False
ballroom.add_item(piano)

# task 5
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)

