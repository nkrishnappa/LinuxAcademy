#!/usr/bin/env python3.6

# string
my_string = "Hello, World!"

"""
print ([letter for letter in my_string])

# OUTPUT: 
# ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
"""
# list
my_list = ["Kavya", "Nandisha", "Nagesh", "Bhavya", "Divya"]

"""
# print (my_list)
'''
for elem in my_list:
    print (elem)
'''
# print([elem for elem in my_list])
"""

# tuple
my_tuple = ("Kavya", "Nandisha", "Nagesh", "Bhavya", "Divya")

"""
# print (my_tuple)
'''
for elem in my_tuple:
    print (elem)
'''
print ([elem for elem in my_tuple])
"""

# Dictionary
my_dict = {"Kavya" : 28, "Nandisha": 27, "Nagesh" : 26 , "Bhavya" : 24, "Divya":21}

"""
# print (my_dict)
'''
for key,value in my_dict.items():
    print (f"Key : {key} \t Value: {value}")
'''
# print ({key:value for (key,value) in my_dict.items()})
"""


