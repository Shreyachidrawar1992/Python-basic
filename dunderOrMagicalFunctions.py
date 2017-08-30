# It is used to emulate builtin types or used to do operator overloading


class Employee:

    def __init__(self,name,lastname,pay):
        self.name = name
        self.lastname = lastname
        self.pay = pay

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.name,self.lastname,self.pay)

    def __str__(self):
        return '{}--{}'.format(self.name,self.lastname)

    def __add__(self, other):
        return self.pay + other.pay

emp1 = Employee('shreya', 'chidrawar', 1100)
emp2 = Employee('shreya', 'chidrawar', 1100)

print emp1 + emp2
print emp1



print 'one'+'two'
Changed file



