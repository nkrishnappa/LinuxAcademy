# -------------------------------------------------------------------
# Python Inheritance
#    Inheritance enables us to define a class that takes all the functionality from a parent class 
#    and allows us to add more.
# 
# It refers to defining a new class with little or no modification to an existing class.
# The new class is called derived (or child) class 
# The one from which it inherits is called the base (or parent) class.

# Base / Parent Class
class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
    def increasePrice(self):
        return self.price * 1.5

# Derived / Child Class
# Derived class inherits features from the base class where new features can be added to it. 
# This results in re-usability of code.
class subCar(Car):
    def __init__(self, model, price):
        super().__init__(model, price)

# subclass = subCar("TATA", 100000)
# print (f'{subclass.price}')           # 100000
# print (f'{subclass.increasePrice()}') # 150000.0

# -------------------------------------------------------
# RealWorld Example:
# Probelem Discription
# 1 . Create a polygon(3 or more sides) Class 
# Data Attributes - 
#    To store the number of sides
#    Magnitude of each side 
# 
# Functions:
#    To get the Inputs of Magnitude of each side
#    To display the sides lengths
#
# 2 . Create a Triangle Class and add the functionality to check the Triangle Area
#  
# TIPS : 
# A polygon is any 2-dimensional shape formed with straight lines. 
# Triangles, quadrilaterals, pentagons, and hexagons are all examples of polygons.
#
# Area of triangle = (Base + hight) / 2
#  
# -------------------------------------------------------
class Polygon:
    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.no_of_sides)]
    def displaySides(self):
        return [print(f'Side {i + 1} is : {self.sides[i]}') for i in range(self.no_of_sides)]

# triangle = Polygon(3)
# triangle.inputSides()
# triangle.displaySides()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# output :
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Enter side 1 : 3
# Enter side 2 : 4
# Enter side 3 : 5
# Side 1 is : 3.0
# Side 2 is : 4.0
# Side 3 is : 5.0
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

# let's say if we want to add the multiple triangle - can we create a derived class?
# Add the additional functionality only for the Triangle
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()
t.inputSides()
t.displaySides()
t.findArea()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# output :
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Enter side 1 : 3
# Enter side 2 : 5
# Enter side 3 : 4
# Side 1 is : 3.0
# Side 2 is : 5.0
# Side 3 is : 4.0
# The area of the triangle is 6.00
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~