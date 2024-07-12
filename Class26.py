from sys import getsizeof

#List and fenarator expressions 
    #Uma forma + rapida para listas, dicionários e etc
    #Menos memoria alocada
    #Valores em bytes

numbers = [x * 10 for x in range(1000000)]
print(type(numbers))
#print(numbers)
print(getsizeof(numbers))

print("===")

numbers = (x * 10 for x in range (1000000))
print(type(numbers))
print(getsizeof(numbers))