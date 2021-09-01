class Pets:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    def sleep(self):
        self.health += 25
        return self
    def eat(self):
        print(self)
        self.health += 10
        self.energy += 5
        return self
    def play (self):
        self.health += 5
    def noise(self):
        return print(f"{self.name} {self.tricks}")