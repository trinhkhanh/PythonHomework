__author__ = 'trinhkhanh'
class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError

class Tiger(Animal):
    def talk(self):
        return 'Woof'

class Elephant(Animal):
    def talk(self):
        return 'A'

class Cat(Animal):
    def talk(self):
        return 'Meo'

class Rabbit(Animal):
    def talk(self):
        return 'eheh'

class Dog(Animal):
    def talk(self):
        return 'Gau'

animals = [Tiger('Woof'), Elephant('A'), Cat('Meo'),Rabbit('eheh'),Dog('Gau')]

for animal in animals:
    print(animal.name, 'keu la', animal.talk())






