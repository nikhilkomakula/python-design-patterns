"""
The Decorator Pattern is a structural pattern used for adding new functionalities to objects dynamically without altering their structure. This type of design pattern comes under structural pattern as this pattern acts as a wrapper for existing classes.
"""

class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 1

class ChocolateDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 3

# Creating a Coffee object
coffee = Coffee()
print("Cost of coffee:", coffee.cost())  # Cost of coffee: 5

# Adding milk to coffee
milk_coffee = MilkDecorator(coffee)
print("Cost of milk coffee:", milk_coffee.cost())  # Cost of milk coffee: 7

# Adding sugar to milk coffee
sugar_milk_coffee = SugarDecorator(milk_coffee)
print("Cost of sugar milk coffee:", sugar_milk_coffee.cost())  # Cost of sugar milk coffee: 8

# Adding chocolate to sugar milk coffee
choco_sugar_milk_coffee = ChocolateDecorator(sugar_milk_coffee)
print("Cost of chocolate sugar milk coffee:", choco_sugar_milk_coffee.cost())  # Cost of chocolate sugar milk coffee: 11