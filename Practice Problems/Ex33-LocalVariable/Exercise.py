# Question:  What will the following script output?
# Please try to do this by mind if you can.

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

"""
Answer : 2

Explanation : At the time when the foo function called, 
the value of the c is 3
But function foo() has the local variable "c" and value 2
so program will return 2

"""