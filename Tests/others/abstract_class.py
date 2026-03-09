from abc import (ABC, abstractmethod)

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat: Meow!")

class Pig(Animal):
    def speak(self):
        print("Pig: Oink!")

rover = Dog()
rover.speak()

kitty = Cat()
kitty.speak()

wilbur = Pig()
wilbur.speak()