#Function map inside a list 

    #muito utilizado com listas
    #apicar uma função a um iterable, por item. (list, tuple, dic etc)

list1 = [1, 2, 3, 4]

def mult(x):
    return x * 2

list2 = map(mult, list1)
print(list(list2))