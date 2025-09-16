import random

nameList = ["John", "Dave", "Mann", "Joe", "Steve", "Sim", "Bobert", "Richard"]

class Fighter:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health
        self.hand = None

    def whats_in_my_hand(self):
        return self.hand

    def take_damage(self, other):
        food = other.whats_in_my_hand()
        self.health -= food.return_lethality()

    def throw(self, other):
        other.take_damage(self)


class Ammo:
    def __init__(self, name, calories, ugliness, brock):
        self.name = name
        self.calories = calories
        self.ugliness = ugliness
        self.broccoli = brock
    def send_info(self):
        print("Object: " + self.name)
        print("Number of calories: " + str(self.calories))
        print("Do you want to eat it? " + str(self.ugliness))
    
    def return_lethality(self):
        if self.broccoli is False:
            return self.calories
        if self.broccoli is True:
            return 1000000

burger = Ammo("Burger", 200, True, False)
broccoliThatKillsYou = Ammo("Normal broccoli", 300, True, True)
meatloaf = Ammo("Meat loaf", 1000, False, False)
salad = Ammo("Salad", 1000, True, False)
footlong = Ammo("Footlong ham and cheese", 600, True, False)
sam = Ammo("Kilometerlong ham and cheese", 100000, False, False)
lettuce = Ammo("Lettuce", 500, True, False)