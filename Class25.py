#List comprehension with numbers

'''value = []

for x in range(6):
    value.append(x * 10)

print(value)'''

value = [x * 10 for x in range(6)]
print(value)
