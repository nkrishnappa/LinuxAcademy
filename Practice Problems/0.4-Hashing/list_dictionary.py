# using the Lists 
stock_list = []
with open(r"C:\Users\nkrishnappa\Desktop\SELF-IMPROVEMENT\ProgrammingLanguageCourse\Practice Problems\0.4-Hashing\stock.csv", "r", encoding='utf-8-sig') as file:
    for line in file:
        tokens = line.split(",")
        stock_date = str(tokens[0])
        stock_price = float(tokens[1])
        stock_list.append([stock_date, stock_price])
print(stock_list)
'''
[['7-Mar', 340.0], ['8-Mar', 380.0], ['9-Mar', 302.0], ['10-Mar', 297.0], ['11-Mar', 323.0], ['12-Mar', 350.0]]
323.0
'''

for element in stock_list:
    if element[0] == "11-Mar":
        print(element[1])

# using the dictionary
stock_list = {}
with open(r"C:\Users\nkrishnappa\Desktop\SELF-IMPROVEMENT\ProgrammingLanguageCourse\Practice Problems\0.4-Hashing\stock.csv", "r", encoding='utf-8-sig') as file:
    for line in file:
        tokens = line.split(",")
        stock_date = str(tokens[0])
        stock_price = float(tokens[1])
        stock_list[stock_date] =  stock_price

print(stock_list)
print(stock_list["11-Mar"])
'''
{'7-Mar': 340.0, '8-Mar': 380.0, '9-Mar': 302.0, '10-Mar': 297.0, '11-Mar': 323.0, '12-Mar': 350.0}
323.0
'''

# Dictionary uses the Hash tables/ Hash Maps
