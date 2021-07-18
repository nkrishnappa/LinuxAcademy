#-------------------------------------------- 
a, b = 4, 12 # 1500489696, 1500489824

print (id(a))  # 1500489696
print (id(b))  # 1500489824
print (id(4))  # 1500489696
print (id(12)) # 1500489824

a, b = 12, 4

print (id(a))  # 1500489824 - a object binds with b object(12) - But 4 object will still be availavble and unbinded state 
print (id(b))  # 1500489696 - b object binds with 4 object
print (id(4))  # 1500489696
print (id(12)) # 1500489824


print(a + b)
print (a.__add__(b))
# 16
# 16
#--------------------------------------------
