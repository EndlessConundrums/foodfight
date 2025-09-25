import random

nameList = ["John", "Dave", "Mann", "Joe", "Steve", "Sim", "Bobert", "Richard", "the cat", "the chef", "Mark", "Timothy", "Carl"]

class Fighter:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health
        self.hand = None
        self.inventory = []

    def get(self, food):
        self.inventory.append(food)
    
    def load(self, index):
        self.hand = self.inventory[index]
        self.inventory.pop(index)

    def say_my_name(self):
        return self.name

    def whats_in_my_hand(self):
        return self.hand

    def take_damage(self, other):
        food = other.whats_in_my_hand()
        self.health -= food.return_lethality()
        if self.health < 0:
            print(self.name + " died")

    def throw(self, other):
        if self.health < 0:
            pass
        fooj = self.whats_in_my_hand()
        other.take_damage(self)
        if fooj.is_broccoli():
            self.take_damage(self)


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
    
    def return_name(self):
        return self.name
    
    def return_lethality(self):
        if self.broccoli is False:
            return self.calories
        if self.broccoli is True:
            return 1000000
    def is_broccoli(self):
        return self.broccoli

burger = Ammo("Burger", 200, True, False)
broccoliThatKillsYou = Ammo("Normal broccoli", 300, True, True)
meatloaf = Ammo("Meat loaf", 1000, False, False)
salad = Ammo("Salad", 1000, True, False)
footlong = Ammo("Footlong ham and cheese", 600, True, False)
sam = Ammo("Kilometerlong ham and cheese", 100000, False, False)
lettuce = Ammo("Lettuce", 500, True, False)

foodList = [burger, broccoliThatKillsYou, meatloaf, salad, footlong, sam, lettuce]

a = Fighter(nameList[random.randint(0, len(nameList) - 1)], random.randint(1, 5), random.randint(500, 1000))
b = Fighter(nameList[random.randint(0, len(nameList) - 1)], random.randint(2, 15), random.randint(250, 750))
c = Fighter(nameList[random.randint(0, len(nameList) - 1)], random.randint(1, 2), random.randint(1000, 5000))
d = Fighter(nameList[random.randint(0, len(nameList) - 1)], random.randint(1, 5), random.randint(500, 1000))
gug = Fighter("gug", 0, 5)




you = Fighter("You", 10, 1000)
fighterList = [a, b, c, d, gug]
for i in fighterList:
    for j in range(3):
        i.get(foodList[random.randint(0, len(foodList) - 1)])

def attack():
    print("Choose ammunition:")
    for i in you.inventory:
        print(i.return_name())
    whatToThrow = input()
    for i in you.inventory:
        if whatToThrow == i.return_name():
            you.load(you.inventory.index(i))
            fooj = you.whats_in_my_hand()
    print("Choose target:")
    for i in fighterList:
        print(i.say_my_name())
    whoToThrowAt = input()
    for i in fighterList:
        if whoToThrowAt == i.say_my_name():
            print("Successfully thrown " + fooj.return_name() + " at " + i.say_my_name())
            you.throw(i)

def foodfight():
    for i in fighterList:
        target = fighterListTwo[random.randint(0, len(fighterListTwo) - 1)]
        print(i.say_my_name() + " attacked " + target.say_my_name())
        i.load(random.randint(0, len(i.inventory) - 1))
        i.throw(target)
        print("")

fighterListTwo = [a, b, c, d, gug, you]
print("It's lunchtime again. What food do you want to pick?")
for i in foodList:
    i.send_info()
for j in range(3):
    whatFood = input()

    for i in foodList:
        if whatFood == i.return_name():
            you.get(i)
            print("You got " + i.return_name())
print("\n")


print("Oh no, a food fight's breaking out!\n")
attack()

print("Watch out, they're throwing things!")
foodfight()

for i in range(3):
    attack()
    print("They're doing it again!")
    foodfight()
    if you.health < 0:
        print("You are dead")
        print("RIP")
        break

print("Everyone ran out of ammunition and the food fight is over.")