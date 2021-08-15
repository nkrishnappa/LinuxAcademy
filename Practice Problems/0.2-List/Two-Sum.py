# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
a = [1, 2, 3, 4, 5 , -3, -4, -6, 10, 20]
number = 6
my_list = []

def twoSum(array:list, number:int) -> tuple:
    global my_list
    for element_x in range(len(array) - 2):
        for  element_y in range(element_x, len(array) - 1):
            if array[element_x] + array[element_y] == number:
                my_tuple = ()
                print(f"{element_x:2} - {array[element_x]:2}, {element_y:2} - {array[element_y]:2} ")
                my_tuple +=  (element_x, element_y)
                my_list.append(my_tuple)
                #return element_x, element_y - function will exit at first match

twoSum(a, number)
print(my_list)