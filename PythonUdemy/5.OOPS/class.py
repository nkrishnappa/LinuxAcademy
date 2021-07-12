# ------------------------------------------
"""
Class Kettle
"""
# class Kettle ():
#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
#         self.on = False


# kenwood = Kettle("Kenwood", 8.99)
# print("{} = {}".format(kenwood.make, kenwood.price))
# Kenwood = 8.99
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
class Point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5
# >>> p1 = Point(6,8)
# >>> p1.distance()
# 10.0
# >>>
# ------------------------------------------

#-------------------------------------------
class A(object):
    @staticmethod
    def stat_meth():
        print("Look no self was passed")
# >>> a = A()
# >>> a.stat_meth()
# Look no self was passed

# >>> type(A.stat_meth)
# <class 'function'>
# >>> type(a.stat_meth)
# <class 'function'>
#-------------------------------------------