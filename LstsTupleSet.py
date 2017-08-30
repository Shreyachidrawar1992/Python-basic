# Lists

#lists are mutable

courses = ['CS', 'Maths', 'Arts', 1]
numbers = [6, 2, 9, 3, 1]
#courses.append('electronics')
#courses.insert(3,'Maths')      #  Can have duplicates
#print courses
Additional_courses = ['Phy', 'Chem']
#courses.append(Additional_courses)
#courses.extend(Additional_courses)
#print courses.pop()
#courses.sort(reverse=True)
#numbers.sort()
#print courses
#print  numbers
#courses.extend(numbers)
#course_str = ' - '.join(courses)
#print course_str
#courseList= course_str.split(' - ')
#print 'courseList is',courseList

for item in courses:        # to prints items inside list
    print 'item is', item

for index, item in enumerate(courses):       # to print item with index
    print 'item is ', item
    print 'index is ', index

######## Tuples ############

# Cant modify tuple unlike list
# Is immutable
# usage- Tuples are faster than list. If you have constant values and wanted to iterate then you can go
# for tuple instead of lists
course_tuple = ('phy','Chem','bio')
#course_tuple1 = course_tuple
#course_tuple[0] = ('dd')
#print course_tuple
print course_tuple
#print course_tuple.index('Chem')

###### Sets #######

# Sets are unordered
# Sets doesnot contain duplicate values
# Mutable
# optimisation to check if the element is present or not as compared to list. KIt internally uses hash table


course_sets = {'maths','chem','physics'}

#print 'chem' in course_sets

course_sets2 = {'Electronics','maths'}
course_sets2.add('Electrical')

#print 'course_sets is',course_sets.intersection(course_sets2)

#print 'course_sets is',course_sets2.difference(course_sets)