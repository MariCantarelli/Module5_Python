#Lambda function

#é uma função(pequena) sem nome
#pode ter vários argumentos mas somente uma expressão
#muito utilizada dentro de outras funções
#codigo mais clean 

'''def add(x):
    return x + 10

print(add(2))'''

add10 = lambda x,y: x + y + 10
print(add10(2, 4))
