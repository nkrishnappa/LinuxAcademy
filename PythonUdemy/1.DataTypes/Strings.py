greeting = "Hello"
# name = input("Please enter your name :")
name = "Nandisha"
print (greeting + ' ' + name)
# Please enter your name :Nandisha
# Hello Nandisha

print(" \"Hi\"... How are you \'Nandisha\'")
# "Hi"... How are you 'Nandisha'
print (' \"Hi\"... How are you \'Nandisha\'')
# "Hi"... How are you 'Nandisha'

print (""" "Hi"... How are you 'Nandisha' """)
# "Hi"... How are you 'Nandisha'


# three single quotes:
string=""" This string has been
split 
over several lines"""
print (string)
# #  this string has been
# # split
# # over several lines

# print ("C:\user\nkrishnappa\notes.text")
# # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape

print("C:\\user\\nkrishnappa\\notes.text")
# C:\user\nkrishnappa\notes.text
print (r'C:\user\nkrishnappa\notes.text')
# C:\user\nkrishnappa\notes.text

greeting="Hello"
name="Nandisha"
age=28

# print (type(greeting))
# print (type(age))
# # <class 'str'>
# # <class 'int'>

print (name + " age is :" )
print (age)
# Nandisha age is :
# 28

# print (name + "age is :" + age) 
# TypeError: can only concatenate str (not "int") to str