#!/usr/bin/env python3.6
from functools import reduce

# map
# using Map collection - square all the elements in an list
'''
domain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# f(x) = x * 2
range_of_values = map(lambda num: num * num, domain)
print (list(range_of_values))

# output - [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

# filter
# using a filter collector , print even number in a list
'''
domain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = filter(lambda num: num % 2 == 0, domain)
print (list(even))

# OUTPUT : [2, 4, 6, 8, 10]
'''

# reduce 
domain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
sum= reduce (lambda accumulator, num: accumulator + num, domain, 0)
     # accumulator = variable which stores the intermidiate results 
     # num = parameter
     # accumulator + num = which gives the sum of iterated numbers
     # domain = List
     # 0 = initially set accumulator with 0
print (sum) 

# OUTPUT = 55
'''
'''

# sorted / reversed
domain = ['nandisha', 'Kavya', 'Nagesh', 'Bhavya', 'divya']

sorted_list=sorted(domain,key=lambda s: s.lower())
print (sorted_list)

reversed_list=reversed(domain)
print (list(reversed_list))

# ['Bhavya', 'divya', 'Kavya', 'Nagesh', 'nandisha']
'''



