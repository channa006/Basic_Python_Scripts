
# Python - Object Oriented Programming
# OOP Allow us to logically group our data and functions
# In a way so it's easy to reuse and also easy to build Upon.

# Data and Functions assocaited with specific class.
# We Call those attributes and methods

# Class is basically a blue prints for creating instances.


# class Employee:
#     pass

# Each Unique Emp we create using Class is the instance of Employeee Class


# emp_1 = Employee()
# emp_2 = Employee()
#
# print(emp_1)
# print(emp_2)

# Instances Variables contain data, that is unique to each intances.
# We can manually create instance variables for each employee

# emp_1.firstname = 'Channabasava'
# emp_1.lastname = 'Kalapurmath'
# emp_1.email = '4uchanna@gmail.com'
# emp_1.pay = 50000
#
# emp_2.firstname = 'Shiva'
# emp_2.lastname = 'Sankar'
# emp_2.email = 'shiva@gmail.com'
# emp_2.pay = 5000000
#
# print(emp_1.email)
# print(emp_2.email)

# We can set all the attribute when they created.
# No need to set all these attributes manually

# Special Init Method , If coming from another language it's constructor
# When we create method within class.
# They receive the instance as first argument automatically.
# After self,we can specify other arguments to accept.


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# By Convention we can call instance self.stick to convention


emp_1 = Employee('Channa', 'Kalapurmath', 50000)
emp_2 = Employee('Shiva', 'Shankar', '500000')

print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.email)
print(emp_2.email)


print(Employee.fullname(emp_2))
