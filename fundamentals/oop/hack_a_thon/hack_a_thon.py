import random
import math

class Character:
    all_characters = []
    def __init__(self, name, health=100, strength=50, speed=50, defense=50):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed
        self.defense = defense
        self.is_alive = True
        Character.all_characters.append(self)
    def print_stats(self):
        print(f"name: {self.name}")
        print(f"health: {self.health}")
        print(f"strength: {self.strength}")
        print(f"speed: {self.speed}")
        print(f"defense: {self.defense}")
        print()
    def attack(self, attackee):
        if not attackee.is_alive:
            print(f"{attackee} is dead already bruh")
        else:
            damage = self.strength * 0.2
            attackee.block(self, damage)
            print(f"{self.name} is attaking {attackee.name} with {damage} damage")
    def block(self, attacker, damage):
            random_num = random.randint(1, 10)
            if random_num >= 9:
                print(f"{self.name} thwarts the attack from {attacker}")
            elif random_num <= 8:
                damage1 = damage * (self.defense/100)
                self.health -= math.floor(damage1)
    def dead(self):
        self.is_alive = False
        print(f"{self.name} has shuffled off this mortal coil")
    @classmethod
    def print_all_characters(cls):
        for character in cls.all_characters:
            character.print_stats()

class Human(Character):
    all_humans = []
    def __init__(self, name, health=100, strength=50, speed=50, defense=50):
        super().__init__(name)
        self.health = health
        self.strength = strength
        self.speed = speed
        self.defense = defense
        Human.all_humans.append(self)

class Monster(Character):
    all_monsters = []
    def __init__(self, name, strength=75, speed=20, defense=65):
        super().__init__(name)
        self.strength = strength
        self.speed = speed
        self.defense = defense
        Monster.all_monsters.append(self)

dumbjock = Human("Dumb Jock", strength=65, speed=35)
dumbblonde = Human("Dumb Blonde", strength=30, defense=20)
dumbhero = Human("Dumb Hero", defense=60)

freddy = Monster("Freddy Kruger")
jason = Monster("Fake Jason", strength=60)

# Character.print_all_characters()
dumbblonde.attack(freddy)
Character.print_all_characters()