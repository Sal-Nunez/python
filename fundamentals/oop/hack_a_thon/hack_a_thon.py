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
        print(self)
        print(f"name: {self.name}")
        print(f"health: {self.health}")
        print(f"strength: {self.strength}")
        print(f"speed: {self.speed}")
        print(f"defense: {self.defense}")
        print()
        return self
    def attack(self, attackee):
        if not attackee.is_alive:
            print(f"{attackee.name} is dead already bruh")
        else:
            damage = self.strength * 0.2
            attackee.block(self, damage)
            print(f"{self.name} is attaking {attackee.name} with {damage} damage")
        return self
    def block(self, attacker, damage):
            random_num = random.randint(1, 10)
            if random_num >= 9:
                print(f"{self.name} thwarts the attack from {attacker.name}")
            elif random_num <= 8:
                damage1 = damage * (self.defense/20)
                self.health -= math.floor(damage1)
                if self.health <= 0:
                    self.dead()
                    print(f"{self.name} kicked the bucket")
            return self
    def skip_turn(self):
        return self
    @classmethod
    def print_all_characters(cls):
        for character in cls.all_characters:
            character.print_stats()

class Human(Character):
    all_humans = []
    dead_humans = 0
    def __init__(self, name, health=100, strength=50, speed=50, defense=50):
        super().__init__(name)
        self.health = health
        self.strength = strength
        self.speed = speed
        self.defense = defense
        Human.all_humans.append(self)
    def dead(self):
        self.is_alive = False
        Human.dead_humans += 1
        print(f"{self.name} has shuffled off this mortal coil")
        return self

class Monster(Character):
    all_monsters = []
    dead_monsters = 0
    def __init__(self, name, strength=75, speed=20, defense=65):
        super().__init__(name)
        self.strength = strength
        self.speed = speed
        self.defense = defense
        Monster.all_monsters.append(self)
    def dead(self):
        self.is_alive = False
        Monster.dead_monsters += 1
        print(f"{self.name} has shuffled off this mortal coil")
        return self

characters = {
    "dumbjock": Human("Dumb Jock", strength=65, speed=35),
    "dumbblonde": Human("Dumb Blonde", strength=30, defense=20),
    "dumbhero": Human("Dumb Hero", defense=60),
    "freddy": Monster("Freddy Kruger"),
    "jason": Monster("Fake Jason", strength=60),
    "pennywise": Monster("Pennywise", defense=20)
}

# Character.print_all_characters()
# dumbblonde.attack(jason)
# dumbhero.attack(jason)
# dumbjock.attack(jason)

# freddy.attack(dumbblonde)
# jason.attack(dumbblonde)
# Character.print_all_characters()

class Game(Character):
    def __init__(self, turn = 1):
        self.turn  = turn
    def human_turn():
        print("Choose your character: dumbjock, dumbblonde, dumbhero")
        user_input = input("choose an option: ")
        while user_input not in ["dumbjock", "dumbblonde", "dumbhero"]:
            user_input = input("not a valid response, try again: ")
        user = characters[user_input]
        print("These are your options: attack or skip_turn")
        user_input = input("choose an option: ")
        while user_input not in ["attack", "skip_turn"]:
            user_input = input("not a valid response, try again: ")
        if user_input == "attack":
            user_input = input("Choose who you want to attack? freddy, jason or pennywise: ")
            while user_input not in ["freddy", "jason", "pennywise"]:
                user_input = input("not a valid response, try again: ")
            user.attack(characters[user_input])
            if Monster.dead_monsters == 3:
                print("Game Over, Humans Win!")
            else:
                print("Monster's turn")
                Game.monster_turn()
        if user_input == "skip_turn":
            user.skip_turn()
            Game.monster_turn()
    def monster_turn():
        print("Choose your character: freddy, jason, pennywise")
        user_input = input("choose an option: ")
        while user_input not in ["freddy", "jason", "pennywise, exit"]:
            user_input = input("not a valid response, try again: ")
        user = characters[user_input]
        print("These are your options: attack or skip_turn")
        user_input = input("choose an option: ")
        while user_input not in ["attack", "skip_turn, exit"]:
            user_input = input("not a valid response, try again: ")
        if user_input == "attack":
            user_input = input("Choose who you want to attack? dumbjock, dumbblonde or dumbhero: ")
            while user_input not in ["dumbjock", "dumbblonde", "dumbhero, exit"]:
                user_input = input("not a valid response, try again: ")
            user.attack(characters[user_input])
            if Human.dead_humans == 3:
                print("Game Over, Monsters Win!")
            else:
                print("Human's turn")
                Game.human_turn()
        if user_input == "skip_turn":
            user.skip_turn()
            Game.human_turn()

Game.human_turn()