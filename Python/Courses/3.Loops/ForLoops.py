#!/usr/bin/env python
print("-------------------------------------------------")

lists = ["Chandhu", "Nandhu", "Divya", "Bhavanika"]
print("------------------------")
print("Loop using for loop")
print("------------------------")
for list in lists:
    print(f"List element {list}")
print("------------------------")
print("Loop using List Comprehensive")
print("------------------------")
print([list for list in lists if list not in ['Divya']])


print("-------------------------------------------------")
tuples = ("Chandhu", "Nandhu", "Divya", "Bhavanika")
for tuple in tuples:
    print (f"List element {tuple}")
print("------------------------")
print("Loop using List Comprehensive")
print("------------------------")
print([tuple for tuple in tuples])


