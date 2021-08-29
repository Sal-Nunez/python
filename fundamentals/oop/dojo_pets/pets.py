class Pets:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    def sleep(self):
        self.pet.health += 25
        return self
    def eat(self):
        self.pet.health += 10
        self.pet.energy += 5
        return self
    def play (self):
        self.pet.health += 5
    def noise(self):
        return print(f"{self.first_name}'s pet {self.pet.name} {self.pet.tricks}")