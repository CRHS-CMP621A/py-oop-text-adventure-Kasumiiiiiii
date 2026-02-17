# character task 1
class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def set_conversation(self, char_conversation):
        self.conversation = char_conversation

    def talk(self):
        print(f"[{self.name} says:] {self.conversation}")
        
    def describe(self):
        print(self.name)
        print(self.describe)

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)