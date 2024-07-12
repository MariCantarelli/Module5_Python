#Function map with lambda

list1 = [1, 2, 3, 4]

'''def mult(x):
    return x * 2

list2 = map(lambda x: x * 2, list1)'''

print(list(map(lambda x: x * 2, list1)))