#!/usr/bin/env python3.6

# Normal Function 
def cube (num):
    return num*num*num

print (cube(5)) # 125



# Lambda Function - Which is Anonymus function
#                   That doesn't have a function name
cube_of_num = lambda num: num*num*num 
'''
# lamda Key
# num - parameter 
# num*num*num - implicit return
'''
print (cube_of_num(5)) # 125





    