# task 2
from room import Room
# challenge 5
from item import Item
# character task 1
from character import Character, Enemy

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

# character task
bob = Character("Bob", "A friendly skeleton")
bob.set_conversation("What's up, dude! Wanna chat?")
kitchen.set_character(bob)
# dave.describe()
# dave.talk()

dave = Enemy("Dave", "A smelly zombie who wants to attack you")
dave.set_conversation("Grrr I want to eat meats and brains...")
dave.set_weakness("knife")
dining_hall.set_character(bob)
# dave.describe()
# dave.talk()

# print("What will you fight with?")
# fight_with = input()
# dave.fight(fight_with)

# challenge 5
knife = Item("Knife")
knife.set_description("A sharp iron knife to fight enemies.")
knife.set_value(30)
kitchen.add_item(knife)

key = Item("Key")
key.set_description("A key to unlock the ballroom door.")
key.set_value(10)
dining_hall.add_item(key)
print(key.get_description())

piano = Item("Piano")
piano.set_description("A grand piano that plays music.")
piano.is_pickable = False
ballroom.add_item(piano)

# task 5
current_room = kitchen
player_inventory = []

while True:
    print("\n")
    current_room.get_details()
    # character task 6
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one to talk to")