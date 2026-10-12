
class Animal:

    def __init__(self, name):
        self.name = name


    def speak(self):
        return "Do a Sound!"


class Dog(Animal):

    def speak(self):
        return "Guau!"

class Cat(Animal):

    def speak(self):
        return "Miau!"


animal = Animal("Zaguate")

print(animal.speak())

dog = Dog("Euro")

print(dog.speak())

cat = Cat("Michi")

print(cat.speak())