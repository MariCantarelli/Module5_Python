from array import array

#Working with array

#Array(matriz)
#   Similar a listas
#   Melhor performance

letters = ['a', 'b', 'c', 'd']
numbers_i = [10, 20, 30, 40]
numbers_f = [1.2, 2.2, 3,2]

print(letters)
print(numbers_i)
print(numbers_f)
print()

letters = array('u', ['a', 'b', 'c', 'd'])
numbers_i = array('i', [10, 20, 30, 40])
numbers_f = array('f', [1.2, 2.2, 3,2])

print(letters)
print(numbers_i)
print(numbers_f)