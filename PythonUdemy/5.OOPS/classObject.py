# ------------------------------------------
"""
Class Kettle
"""
class Kettle ():
    power_source = "Electric"
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
hamilton = Kettle("Hamilton", 14.55)

print("{} = {}".format(kenwood.make, kenwood.price))
# Kenwood = 8.99

print (kenwood.on)      # False
kenwood.switch_on()
print (kenwood.on)      # True
Kettle.switch_on(kenwood)
print (kenwood.on)      # True

kenwood.power = 1.5     # power variable bound to an specific instance of an class
print (kenwood.power)   # 1.5
# print (hamilton.power)  # AttributeError: 'Kettle' object has no attribute 'power'

print (Kettle.power_source)     # Electric
print (hamilton.power_source)   # Electric
print (kenwood.power_source)    # Electric

# Access the Object Namespace
# A dictionary or other mapping object used to store an object's (writable) attributes.
print (Kettle.__dict__)
print (hamilton.__dict__)
print (kenwood.__dict__)
"""
{'__module__': '__main__', 'power_source': 'Electric', '__init__': <function Kettle.__init__ at 0x0097F2F8>, 'switch_on': <function Kettle.switch_on at 0x0097F2B0>, '__dict__': <attribute '__dict__' of 'Kettle' objects>, '__weakref__': <attribute '__weakref__' of 'Kettle' objects>, '__doc__': None}
{'make': 'Hamilton', 'price': 14.55, 'on': False}
{'make': 'Kenwood', 'price': 8.99, 'on': True, 'power': 1.5}
"""
Kettle.power_source = "atomic"

print (Kettle.power_source)     # atomic
print (hamilton.power_source)   # atomic

# hamilton.power_source = "gas"   # gas
# print (hamilton.power_source)   # gas

print (kenwood.power_source)    # atomic

print (Kettle.__dict__)
print (hamilton.__dict__)
print (kenwood.__dict__)

"""
atomic
atomic
atomic
{'__module__': '__main__', 'power_source': 'atomic', '__init__': <function Kettle.__init__ at 0x0365F2F8>, 'switch_on': <function Kettle.switch_on at 0x0365F2B0>, '__dict__': <attribute '__dict__' of 'Kettle' objects>,
'__weakref__': <attribute '__weakref__' of 'Kettle' objects>, '__doc__':
None}
{'make': 'Hamilton', 'price': 14.55, 'on': False}
{'make': 'Kenwood', 'price': 8.99, 'on': True, 'power': 1.5}
"""


del kenwood
# ------------------------------------------

# ------------------------------------------
"""
Class Point
NOTE - Ran this in Terminal

TIP : Distance between any point (x, y) in 
xy-plane and the origin (0, 0) is
sqrt{x^2~+~y^2}
(6,5) - (6**2 + 8**2) ** 0.5 = 10.0

Finding Sqrt in Pythan
- x**.5 or math.sqrt(x)?
"""
# class Point(object):
#     def __init__(self,x = 0,y = 0):
#         self.x = x
#         self.y = y

#     def distance(self):
#         return (self.x**2 + self.y**2) ** 0.5
# >>> p1 = Point(6,8)
# >>> p1.distance()
# 10.0
# >>>
# ------------------------------------------

#-------------------------------------------
# class A(object):
#     @staticmethod
#     def stat_meth():
#         print("Look no self was passed")
# >>> a = A()
# >>> a.stat_meth()
# Look no self was passed

# >>> type(A.stat_meth)
# <class 'function'>
# >>> type(a.stat_meth)
# <class 'function'>
#-------------------------------------------