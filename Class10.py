#Tuples
    #Armazenar + de uma informação em variaveis 
    #Manter a sequencia dos dados em uma variavel
    #Não podem ser alterados(Immutable)

colors_list = ['yellow', 'green', 'blue', 'red']
colors_tuple = ('yellow', 'green', 'blue', 'red')

'''print(type(colors_list))
print(type(colors_tuple))

two_lists = colors_tuple * 2
print(two_lists)'''

colors_tuple.append('Purple')
print(colors_tuple)