# insert() function counts the number of occurrences of the item being inserted into the dictionary. 

total = {}
print(id(total))
def insert(items:str) -> None:
    if items in total:
        total[items] += 1
    else:
        total[items] = 1
    print (id(total))

insert("Apple")
insert("Orange")
insert("Apple")

print(total)
print(len(total))