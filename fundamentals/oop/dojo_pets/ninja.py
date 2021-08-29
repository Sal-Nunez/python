from pets import Pets
class Ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        Pets.play(self)
        return self
    def feed(self):
        Pets.eat(self)
        return self
    def bathe(self):
        Pets.noise(self)
        return self
alexa = Ninja("Alexa", "Amazon", "Beef Jerky", "Purina", "Dog")
alexa.pet = Pets('Sparky', 'Labrador', 'Plays Dead')
john = Ninja('John', 'Appleseed', 'Snake Treat', 'Rats', 'Snake')
john.pet = Pets('Danger Noodle', 'King Cobra', 'Bites')
alexa.feed()
alexa.walk()
alexa.bathe()
john.bathe()