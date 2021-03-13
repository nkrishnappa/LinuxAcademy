#!/usr/bin/env python3.6

# string
my_string = "Hello, World!"

"""
print ([letter for letter in my_string])

# OUTPUT: 
# ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
"""
'''
# 1. Access
print (my_string[1])
#   e
print (my_string[0:]) # start :
#   Hello, World!
print (my_string[2:3]) # start:stop
#   l
print (my_string[2:10:2]) # start:stop:increment
#   lo o
'''

'''
2. Insert
my_string[1]="E"
print (my_string)
# Error :
#     my_string[1]="E"
#     TypeError: 'str' object does not support item assignment
# Strings are immutable, so you can't change their characters in-place.


3. Delete
del my_string
print (my_string) # NameError: name 'my_string' is not defined
'''

# list
my_list = ["Kavya", "Nandisha", "Nagesh", "Bhavya", "Divya"]

'''
1. Access
print (my_list[0]) # -> Kavya
print (my_list[2:]) # -> ['Nagesh', 'Bhavya', 'Divya']
print (my_list[1:3]) # -> ['Nandisha', 'Nagesh']
print (my_list[0:len(my_list):1]) # start:end:step
# ['Kavya', 'Nandisha', 'Nagesh', 'Bhavya', 'Divya']
print (my_list[0:len(my_list):2]) # start:end:step
# ['Kavya', 'Nagesh', 'Divya']

print (my_list[-1])
# Divya
print (my_list[:-1])
# ['Kavya', 'Nandisha', 'Nagesh', 'Bhavya']
'''

'''
2. Insert

my_list[1] = "NandishaKrishnappa"
print ([list for list in my_list])
# print ([list+list for list in my_list])


my_list.append("Chandhu")
# ['Kavya', 'Nandisha', 'NageshKrishnappa', 'Nagesh', 'Bhavya', 'Divya']
my_list.insert(2,"NageshKrishnappa")
# ['Kavya', 'Nandisha', 'NageshKrishnappa', 'Nagesh', 'Bhavya', 'Divya', 'chandhu']
print (my_list.index("Chandhu")) # 6 

print ([list for list in my_list])
print (sorted(my_list))
my_list.sort()
print (my_list)
# ['Bhavya', 'Divya', 'Kavya', 'Nagesh', 'NageshKrishnappa', 'Nandisha', 'chandhu']
'''
'''
3. Delete

del my_list[1]
print (my_list)
del my_list[1:2]
print (my_list)
del my_list[0:len(my_list):2]
print (my_list)
del my_list
print (my_list)
'''
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
# tuple has fixed length. List has mutable nature, tuple has immutable nature.
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
#Double The Age
print ({key:value*2 for (key,value) in my_dict.items()})