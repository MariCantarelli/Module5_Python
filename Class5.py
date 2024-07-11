#Extracting variables from lists

products  = ['arroz', 'feijão', 'laranja', 'banana', 4, 5, 6, 7]
#                0       1           2           3

#item1, item2, item3, item4 = products precisa chamar todos dessa forma 
item1, item2, *outros, item3 = products

'''item1 = products[0]
item2 = products[1]
item3 = products[2]
item4 = products[3]'''

print(item1)
print(item2)
print(item3)
print(outros)
#print(item4)