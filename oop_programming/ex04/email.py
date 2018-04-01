

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Test', 'User')
emp_2 = Employee('John', 'Smith')

print (emp_1.email)
print (emp_2.email)
print("")
print (emp_1.fullname())
print (emp_2.fullname())
