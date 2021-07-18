# class Definition
# 1. Class : A class is a blueprint for the object.

class Car:

    type = "vehicle"

    # __new__ - __new__() is called before __init__(). 
    # We can also see that the parameter cls in __new__() is the class itself (Car).
    # Finally, the object is created by calling the __new__() method on the object base class.
    def __new__(cls, *args, **kwargs):
        print ("Hello! We are @ __new__")
        obj = super().__new__(cls)
        return obj

    # __init__ Constructor? 
    # It does not have any return type.
    # A constructor is automatically called when an object is created.
    
    # Instance attributes
    def __init__(self, model, price):
        self.model = model
        self.price = price
        print ("Hello! you are in __init__")                          # Honda = Car("city", "1000000")  # Hello! you are in __init__
        # return self.model                                           # TypeError: __init__() should return None, not 'str'

    # Member Functions
    # All members in a Python class are public by default. 
    # Any member can be accessed from outside the class environment.
    def increasePrice(self):
        return self.price * 1.5

# Inheritance Baseclass - Car , Derived/child Class - superCar 
class superCar(Car):
    pass

# 2. Object : An object (instance) is an instantiation of a class. 
# When class is defined, only the description for the object is defined. 
# Therefore, no memory or storage is allocated.

# Instantiate the Car class - Object/Instance of a class
Honda = Car("city", 1000000)
print (f' Price Before Price Hike - {Honda.price}\n Price After the Price Hike - {Honda.increasePrice()}')
#  Price Before Price Hike - 1000000
#  Price After the Price Hike - 1500000.0
# --------------------------------------------
# Accessing Attributes
# --------------------------------------------
# access the class attributes
print (f'Honda is - {Honda.type}')                            # Honda is - vehicle

# access the instance attributes
print (f'Car Hondas model - {Honda.model} Price - {Honda.price}') # Car Hondas model - city Price - 1000000

print (f'Honda instance or Object type : {type(Honda)}')          # <class '__main__.Car'>
print (f'Car type : {type(Car)}')                                 # <class 'type'>

# Inheritance
Honda = superCar("city", 1000000)
print (f'Honda instance or Object type : {type(Honda)}')          # <class '__main__.superCar'>
print (f'Car type : {type(Car)}')                                 # <class 'type'>
print (f'Car Hondas model - {Honda.model} Price - {Honda.price}') # Car Hondas model - city Price - 1000000

# -------------------------------------------------------
# $ C:/Users/nkrishnappa/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/nkrishnappa/Desktop/SELF-IMPROVEMENT/ProgrammingLanguageCourse/PythonUdemy/5.OOPS/concepts.py
# Honda instance or Object type : <class '__main__.Car'>
# Car type : <class 'type'>
# Car Hondas model - city Price - 1000000
# Honda instance or Object type : <class '__main__.superCar'>
# Car type : <class 'type'>
# Car Hondas model - city Price - 1000000
# -------------------------------------------------------