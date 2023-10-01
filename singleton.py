"""
The Singleton pattern ensures a class has only one instance and provides a global point of access to it.
"""
class Singleton:
    _instance = None

    # cls refers to the class, whereas self refers to the instance
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
# create first instance
singleton1 = Singleton()
print(f"singleton1: {singleton1}")

# set a variable against singleton1
singleton1.n = 10
print(f"singleton1.n: {singleton1.n}")

# create second instance
singleton2 = Singleton()
print(f"singleton2: {singleton2}")

# set a variable against singleton2
singleton2.n = 20
print(f"singleton2.n: {singleton2.n}")

# print the variable against singleton1
print(f"singleton1.n: {singleton1.n}")