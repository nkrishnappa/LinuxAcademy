# --------------------------------------------
# Python Sequence types
# 1. The String Type

# --------------------------------------------
# String Type
# a. concatination
string1= "Hello "
string2= "World"
print (string1 + string2 ) # Hello World
print ("Hello " "World")   # Hello World

# b. operations
print ("Hello " * 3)       # Hello Hello Hello
print ("Hello " * (5 - 2) + "3" )  # Hello Hello Hello 3

# c. conditions
today = "sunday"
print ("day" in today)    # True
print ("mon" in today)    # False

# --------------------------------------------
# String Replacement Fields - using str()
Age=30
print ("My age is " + str(Age) + " years") # My age is 30 years

# Format Method:
print ("My age is {0} years".format(Age))  # My age is 30 years

print ("There are {0} days in {1}, {2}, {3}"\
    .format(31,"Jan","Mar","May"))         # There are 31 days in Jan, Mar, May

print ("Jan: {2}, Feb: {0}, Apr : {1}"\
    .format(28,30,31))                     # Jan: 31, Feb: 28, Apr : 30

print (""" 
Jan : {2}
Feb : {0}
Apr : {1}
""".format(28,30,31))    
# Jan : 31
# Feb : 28
# Apr : 30

# --------------------------------------------
# String Formating: 
for num in range(8,12):
    print ("No. {0} square : {1} cube   : {2}".format(num,num**2, num**3))
# No. 8 square : 64 cube   : 512
# No. 9 square : 81 cube   : 729
# No. 10 square : 100 cube   : 1000
# No. 11 square : 121 cube   : 1331

# formating properly by setting the length
for num in range(8,12):
    print ("No. {0:2} square : {1:4} cube   : {2:4}".format(num,num**2, num**3))
# No.  8 square :   64 cube   :  512
# No.  9 square :   81 cube   :  729
# No. 10 square :  100 cube   : 1000
# No. 11 square :  121 cube   : 1331

# Numbers Alien properly -  left (<) right (>) center (^)
for num in range(8,12):
    print ("No. {0:^2} square : {1:<4} cube   : {2:>4}".format(num,num**2, num**3))
# No. 8  square : 64   cube   :  512
# No. 9  square : 81   cube   :  729
# No. 10 square : 100  cube   : 1000
# No. 11 square : 121  cube   : 1331

# Setting precision
print ("Pi is approximately {0:12}".format(22/7))     # Pi is approximately 3.142857142857143
print ("Pi is approximately {0:12f}".format(22/7))    # Pi is approximately     3.142857
print ("Pi is approximately {0:12.50f}".format(22/7)) # Pi is approximately 3.14285714285714279370154144999105483293533325195312
print ("Pi is approximately {0:52.50f}".format(22/7)) # Pi is approximately 3.14285714285714279370154144999105483293533325195312
print ("Pi is approximately {0:62.50f}".format(22/7)) # Pi is approximately           3.14285714285714279370154144999105483293533325195312
print ("Pi is approximately {0:72.50f}".format(22/7)) # Pi is approximately                     3.14285714285714279370154144999105483293533325195312
print ("Pi is approximately {0:<72.50f}".format(22/7))# Pi is approximately 3.14285714285714279370154144999105483293533325195312
print ("Pi is approximately {0:<72.54f}".format(22/7))# Pi is approximately 3.142857142857142793701541449991054832935333251953125000

# --------------------------------------------
# f-strings
print (f"Pi is approximately {22/7:12.50f}") # Pi is approximately 3.14285714285714279370154144999105483293533325195312
pi = 22 / 7
print (f"Pi is approximately {pi:12.50f}")   # Pi is approximately 3.14285714285714279370154144999105483293533325195312

greeting="Hello"
name="Nandisha"
age=28
# print (name + "age is :" + age) 
# TypeError: can only concatenate str (not "int") to str

print (name + f" is {age} years old") # Nandisha is 28 years old

# --------------------------------------------
# python 2 string Interpolation - printf (supported in python 2 , in 3 it's deprecated)
# works same as c - printf

age = 24 
major = "years"
minor = "months"
print ("My age is %d years" % age) # My age is 24 years
print ("My age is %d %s, %d %s" %(age, major, 12, minor))
# My age is 24 years, 12 months

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
# Below all will print 12345678
print(data[::5])
print(data[0:-1:5])
print(data[:-1:5])
# --------------------------------------------
# --------------------------------------------
print (45 - 15 / 3) # 40.0 
 # b / c will be calculated first, to give 45 - 5.0 Because the division gives a float, the result will also be a float.
