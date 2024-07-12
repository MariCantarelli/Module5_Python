#List comprehension with strings
    #mais so,simples de se escrever
    #utilizado quando você precisa criar uma nova lista a partir de uma existente

fruits1 = ['avocato', 'banana', 'strawberry', 'kiwi', 'pineapple']
#fruits2 = []

'''for itens in fruits1:
    if 'b' in itens:
        fruits2.append(itens)'''

fruits2 =[item for item in fruits1 if 'k' in item]
print(fruits2)