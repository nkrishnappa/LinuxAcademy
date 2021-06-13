a = 20
b = 10

print ( a + b )  # 30
print ( a - b )  # 10
print ( a * b )  # 200
print ( a / b ) # 2
print ( a // b ) # 2
print ( a % b )  # modulas - 0

# Remenber Python is Strictly typed 
for num in range (a):
    print(num)

# prints 0 - 19, However 
# for num in range ( a / b ):
#     print(num)
# TypeError: 'float' object cannot be interpreted as an integer

# Solution : Use the Integer devision operator
for num in range ( a // b ):
    print(num)

# Expressions 
print(a + b / 3 - 4 * 12)      # -24.666666666666668
print(a + (b /3 ) - (4 * 12))  # -24.666666666666668
print( ( (a + b) /3 -4) * 12)    # 72.0
