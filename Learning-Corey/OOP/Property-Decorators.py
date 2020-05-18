# How to use property decorators
# Getters , setters and deleters- class attributes


# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
# # One way to accomplish - but it need changes for everyone
#
#     def email(self):
#         return '{}.{}@company.com'.format(self.first, self.last)
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# emp_1 = Employee('Channa', 'Kalapurmath')
#
# emp_1.first = 'Chand'
#
# print(emp_1.fullname())
# print(emp_1.email())


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
# Other way setting property
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Name Deleted!')
        self.first = None
        self.last = None


emp_1 = Employee('Channa', 'Kalapurmath')

emp_1.first = 'Chand'

# Cannot set Full name attribute , For Ex
emp_1.fullname = 'Channabasava Kalapurmath'

print(emp_1.fullname)
print(emp_1.email)


del emp_1.fullname
