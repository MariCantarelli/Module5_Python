#Loop inside dictionary

student = {'name': 'ana', 'age': 16, 'final_grade': 'A', 'approval': True}

'''for x in student.values():
    print(x)

for x in student.keys():
    print(x)'''

for keys,values in student.items():
    print(keys, values)