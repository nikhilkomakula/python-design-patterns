"""
The Factory Method pattern provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
class AnimalFactory:
    @classmethod
    def create_animal(cls, animal_type):
        try:
            return eval(animal_type)().speak()
        except Exception as e:
            raise ValueError(f"Animal Type '{animal_type}' is not supported! - {e}")


print(AnimalFactory.create_animal("Dog"))