from random import randint

class Goblin:

    def __init__(self, name, hp = 20):
        self.name = name
        self.hp = hp
        self.type = "goblin"
        self.speed = randint (5, 10)
        self.power = randint (5, 10)
        self.armor_rating = 1
        self.weapon = randint(1, 3)
        if self.weapon == 1:
            self.weapon = "knife"
            self.power *= 0.5
        elif self.weapon == 2:
            self.weapon = "sword"
        else:
            self.weapon = "ax"
            self.power *= 1.5

    def speak(self):
        print(f"the type of the monster: {self.type}, and her name is: {self.name}")

    def attack(self):
        pass