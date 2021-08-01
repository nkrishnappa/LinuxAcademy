# Question:  Why is there an error in the code, 
# and how would you fix it?

def foo(a=1, b=2):
    return a + b
 
x = foo - 1

"""
Answer :
TypeError: unsupported operand type(s) for -: 'function' and 'int'

type(foo)   - <class 'function'>
type(foo()  - <class 'int'>

Ideally the code shoud be - 
x = foo() - 1
"""