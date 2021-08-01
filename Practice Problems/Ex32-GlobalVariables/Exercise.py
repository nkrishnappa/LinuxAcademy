# Question:  What will the following script output?
# Please try to do this by mind if you can.

c = 1
def foo():
    return c
c = 3
print(foo())

"""
Answer : 3

Explanation : At the time when the foo function called, 
the value of the c is 3
"""