#Updating dictionary items

student = {'name': 'ana', 'age': 16, 'final_grade': 'A', 'approval': True}

#student['name'] = 'Jose'
#student.update({'name': 'Jose', 'final_grade': 'B'})
#student.update({"address": 'Street A'})
#print(student.get('address', 'dont exist'))

del student['age']
print(student)