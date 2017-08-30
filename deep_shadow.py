from copy import deepcopy, copy


a = 10
b = copy(a)
print 'id of b is', id(a)
print 'id of b is', id(b)
b = 11
print 'id of b is', id(b)
print 'value of a is', a
abc = list()
abc = zip([1,2],[5,6,7],[10,11,12],[5,7,8,9])
print abc

help(zip)
'''
a = [1,2,3,4]
#b = a
b = copy(a)
#b = deepcopy(a)
print 'address of a is', id(a)
print 'address of b is', id(b)
'''