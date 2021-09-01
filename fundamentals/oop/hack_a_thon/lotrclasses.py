'''
Lord of the Rings

- Race
    - Hobbit
    - Human
    - Wizard
    - Elf

Action
-Race
    -speak
    -attack
    -

- Hobbit
    - 
- Human
    - 
- Wizard
    - Lose Mana
- Elf
    - Lose Mana
'''

class Race:
    all_characters = []
    def __init__(self, name, health=100, strength=50, speed=50, defense=50, mana=5):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed
        self.defense = defense
        self.mana = mana
        self.is_alive = True
        Race.all_characters.append(self)
    def print_stats(self):
        print(f"name: {self.name}")
        print(f"health: {self.health}")
        print(f"strength: {self.strength}")
        print(f"speed: {self.speed}")
        print(f"defense: {self.defense}")
        print(f"mana: {self.mana}")
        print()
    def attack(self, attackee):
        if attackee.is_alive <= 0:
            print("stop beating the dead man!")
        else:
            damage = self.strength * 0.1
            attackee.block(self, damage)
            if self.health <= 0:
                self.dead()
    def block(self, attacker, damage):
        self.health -= damage
        print(f"{self.name} is getting attacked by {attacker.name} doing {damage} damage")
    def dead(self):
        self.is_alive = False
        print(f"{self.name} is dead")
    @classmethod
    def print_all_characters(cls):
        for character in cls.all_characters:
            character.print_stats()

class Hobbit(Race):
    all_hobbits = []
    def __init__(self, name, strength=20, speed=70, defense=25):
        super().__init__(name)
        self.strength = strength
        self.speed = speed
        self.defense = defense
        Hobbit.all_hobbits.append(self)

    @classmethod
    def print_hobbits(cls):
        for hobbit in cls.all_hobbits:
            hobbit.print_stats()

class Human(Race):
    all_humans = []
    def __init__(self, name, strength=20, speed=70, defense=25):
        super().__init__(name)
        self.strength = strength
        self.speed = speed
        self.defense = defense
        Human.all_humans.append(self)

    @classmethod
    def print_humans(cls):
        for human in cls.all_humans:
            human.print_stats()

class Wizard(Race):
    all_wizards = []
    def __init__(self, name, strength=20, speed=70, defense=25):
        super().__init__(name)
        self.strength = strength
        self.speed = speed
        self.defense = defense
        Wizard.all_wizards.append(self)

    @classmethod
    def print_wizards(cls):
        for wizard in cls.all_wizards:
            wizard.print_stats()

bilbo = Hobbit("Bilbo")
strongbad = Hobbit("Strongbad", strength=45, speed=45)

# bilbo.print_stats()
# strongbad.print_stats()
Race.print_all_characters()
print(strongbad.health)
bilbo.attack(strongbad)
print(strongbad.health)