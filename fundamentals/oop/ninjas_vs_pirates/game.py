from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
def battle(fighter1, fighter2):
    if (fighter1.health <= 0):
        print ("Jack Sparrow Wins the Battle")
    elif (fighter2.health <= 0):
        print ("Michelangelo Wins the Battle")
    else:
        fighter1.attack(fighter2)
        fighter2.attack(fighter1)
        print(f"{fighter1.name} Health: {fighter1.health}\n{fighter2.name} Health: {fighter2.health}")
        battle(fighter1, fighter2)
battle(michelangelo, jack_sparrow)