# Classes allow us to logically group data nad function so that easy to reuse. Data - attribute, Functions
# Its a blueprint for creating instances
import __builtin__
class Employee:

    '''
    Employee Class
    '''
    def __init__(self,name,lastname,rollno,email):
        self.name = name
        self.lastname = lastname
        self.rollno = rollno
        self.email = email

    def fullname(self):
        return '{}{}'.format(self.name, self.lastname)

emp1 = Employee('shreya','chidrawar',12,'shreyachidrawar1992')
emp2 = Employee('sreenu','pasikanti',12,'spasikan@cisco.com')
print emp1.name
print emp2.fullname()
print dir(__builtin__)