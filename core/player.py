from random import randint

class Player:

    def __init__(self, name, hp = 50):
        self.name = name
        self.hp = hp
        self.speed = randint(5, 10)
        self.power = randint(5, 10)
        self.armor_rating = randint (5, 15)
        self.profession = randint (1, 2)
        if self.profession == 1:
            self.profession = "warrior"
            self.power += 2
        else:
            self.profession = "cure"
            self.hp += 10

    def speak(self):
        print(f"hello my name is: {self.name}. and I'm a {self.profession}")

    def attack(self):
        pass