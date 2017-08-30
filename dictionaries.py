
student = {'name': 'shreya', 'age': '25', 'courses':['Maths','science']}

#print student['name']       # gives error for keys not present

#print student.get('courses')      # gives None for keys not present

# for keys in student:
#     print 'key is',keys

# for key,value in student.items():
#     print 'key and value are', key,value

#student['name'] = 'abc'

student.update({'name': 'abc', 'age': 26})
#del(student['name'])
#student.pop('name')
print student