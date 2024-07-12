#Viewing itens, keys and values

student = {
    'name': 'ana', 
    'age': 16, 
    'final_grade': 'A', 
    'approval': True, 
    'Subjects': ['Math', 'English', 'Physical']
    }

'''print(student)
print(student.get('Subjects'))
print(len(student))'''

print(student.items())
print(student.keys())
print(student.values())