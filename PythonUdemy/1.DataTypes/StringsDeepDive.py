# --------------------------------------------
# Positive Indexing : 
parrot = "Norwegian Blue"
#         012345678901234

print (parrot)      # Norwegian Blue
print (parrot [3])  # w
print (parrot [13]) # e
# print (parrot [14]) # IndexError: string index out of range

# --------------------------------------------
# Negative Indexing 

parrot = "Norwegian Blue"
#         43210987654321           
print (parrot [-1])  # e
print (parrot [-13]) # 0
print (parrot [-14]) # N
# print (parrot [-15]) # IndexError: string index out of range

# --------------------------------------------
# String Slicing - Positive 
parrot = "Norwegian Blue"
#         012345678901234
print (parrot [0:6])    # Norweg
print (parrot [3:5])    # We
print (parrot [0:9])    # Norwegian
print (parrot [:9])     # Norwegian
print (parrot [10:14])  # Blue
print (parrot [10:])    # Blue

print (parrot [:6] + \
       parrot [6:])     # Norwegian Blue
print (parrot [:])      # Norwegian Blue

# --------------------------------------------
# String Slicing - Negative
parrot = "Norwegian Blue"
#         43210987654321    

print (parrot [-4:])    # Blue
print (parrot [-14:-8]) #  Norweg

# --------------------------------------------
# String Slicing - Positive 
parrot = "Norwegian Blue"
#         012345678901234
print (parrot [0:6:3])    # Nw
print (parrot [3:10:2])   # Wga
print (parrot [0:9:3])    # Nwi


number = "9,223,372,036,545,543,435"
print (number[1::4])      # ,,,,,,
seperators= number[1::4]

number = "9,223 372:036-545,543,435"
print (number[1::4])      # , :-,,
seperators= number[1::4]

# Best use case:
values= "".join(char if char not in seperators else " " for char in number).split()
print (values) # ['9', '223', '372', '036', '545', '543', '435']
print ([int(val) for val in values]) # [9, 223, 372, 36, 545, 543, 435]

# --------------------------------------------
# Slicing Backwards
alpha="abcdefghijklmnopqrstuvwxyz"

print (alpha [25::-1])   # zyxwvutsrqponmlkjihgfedcba
print (alpha [::-1])     # zyxwvutsrqponmlkjihgfedcba
print (alpha [4::-1])    # edcba
print (alpha [16:13:-1]) # qpo
print (alpha [:-9:-1])   #  
print (alpha [17:3:-1])
print (alpha [17:3])
# --------------------------------------------
# --------------------------------------------

