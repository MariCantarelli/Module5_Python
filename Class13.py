#Functions in set

#Set (listas)
    #Evita itens duplicados
    #Não utiliza index

#list1 = [1, 2, 3, 4, 5, 6]
s1 = {1, 2, 3, 4, 5, 6, 1, 2}
#s1.add(4)
s1.update([6, 7, 8, 9, 10])
s1.remove(10) #so funciona com o que tem na lista
s1.discard(9) #funciona com o que não tem na lista

#print(list1)
print(s1)
'''print(type(list1))
print(type(s1))'''