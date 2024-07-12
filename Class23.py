#Function Filter

value = [10, 12, 34, 44, 57]

'''def remove20(x):
    return x > 20

print(list(filter(remove20, value)))'''

print(list(filter(lambda x: x > 20, value)))