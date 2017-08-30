# Classes allow us to logically group data nad function so that easy to reuse. Data - attribute, Functions
# Its a blueprint for creating instances

class Employee:

    """
    Is a Employee class
    """
    no_emp = 0
    raise_amount = 1.04
    def __init__(self,name,lastname,rollno,email):
        self.name = name
        self.lastname = lastname
        self.rollno = rollno
        self.email = email

    def fullname(self):
        return '{}{}'.format(self.name,self.lastname)

emp1 = Employee('shreya','chidrawar',12,'shreyachidrawar1992')
emp2 = Employee('sreenu','pasikanti',12,'spasikan@cisco.com')
print Employee.raise_amount
print emp1.raise_amount

print 'before', emp1.__dict__
emp1.raise_amount = 1.08
print 'After', emp1.__dict__
print 'Employee dict',Employee.__dict__

print 'emp2 is',emp2.raise_amount

