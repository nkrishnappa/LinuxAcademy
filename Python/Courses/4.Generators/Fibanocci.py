#!/usr/bin/env python3.6

# using generator - print simple range type function
def genFib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

'''
>>> list(genFib())
^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "Fibanocci.py", line 7, in genFib
    a, b = b, a + b
KeyboardInterrupt

# python3.6 -i Fibanocci.py 
>>> fib = genFib()
>>> next(fib)
1
>>> next(fib)
1
>>> next(fib)
2
>>> next(fib)
3
>>> next(fib)
5
>>> 

[root@localhost 4.Generators]# python3.6 -i Fibanocci.py 
>>> fib = genFib()
>>> [next(fib) for _ in range(50)]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]
>>> exit()


[root@localhost 4.Generators]# python3.6 -i Fibanocci.py 
>>> fib = genFib()
>>> [next(fib) for _ in range(50)] [-1]
12586269025

'''
