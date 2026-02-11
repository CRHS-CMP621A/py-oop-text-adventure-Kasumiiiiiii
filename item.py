# challenge 5
class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.is_pickable = True
        self.value = 0

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.descrption = item_description


    def set_value(self, gold_value):
        self.value = gold_value

    def get_value(self):
        return self.value
    
    def show_info(self):
        print(f"item: {self.name}")
        print(f"description: {self.description}")
        print(f"value: {self.value} coin")