#----------------------------------------------------
# if Conditions

# name = input("Name Please  :")
# age = int(input("How old you are {0}? ".format(name)))
name = "Nandisha"
age = 22


if age > 18 :
    print ("Congratulations! you are eligible")
else:
    print ("sorry! you are not eligible")

# Name Please  :Nandisha
# How old you are Nandisha? 27
# Congratulations! you are eligible

#----------------------------------------------------
# Deep Dive onto If loop
guess = int(input("please enter the number between 1 -10 :"))

if guess < 5:
    print ("Guess higher number please... ")
elif guess > 5:
    print ("Guess lower number please... ")
else:
    print ("you got it first time !")

# please enter the number between 1 -10 :5
# you got it first time !

# please enter the number between 1 -10 :3
# Guess higher number please...
#----------------------------------------------------

