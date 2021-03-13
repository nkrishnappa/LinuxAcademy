#!/usr/bin/env python3.6


# Create Generator
'''
It is fairly simple to create a generator in Python. 
It is as easy as defining a normal function, but with a yield statement instead of a return statement.

If a function contains at least one yield statement (it may contain other yield or return statements),
it becomes a generator function. Both yield and return will return some value from a function.

The difference is that while a return statement terminates a function entirely,
yield statement pauses the function saving all its states and later continues from there on successive calls.
'''

# using generator - print simple range type function
def generator(stop,start=1,step=1):
    num=start
    while num <= stop:
        yield num
        num +=step

gen=generator(10)

"""
[root@localhost 4.Generators]# python3.6 -i Gen.py 
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
>>> next(gen)
4
>>> next(gen)
5
>>> next(gen)
6
>>> next(gen)
7
>>> next(gen)
8
>>> next(gen)
9
>>> next(gen)
10
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
>>> for num in generator(10):
...     print (num)
... 
1
2
3
4
5
6
7
8
9
10
>>> 
>>> exit()

>>> for num in generator(100,start=1,step=5):
...     print (num)
... 
1
6
11
16
21
26
31
36
41
46
51
56
61
66
71
76
81
86
91
96
>>> for num in generator(100,start=0,step=5):
...     print (num)
... 
0
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100

"""