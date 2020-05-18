# Magic/Dunder Methods
# Operators Overload - emulate build in functions
# Special Methos - allows to modify built in functionality and operations
# Special Methods -Always surrounded by __init__(dunders)


class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# __repr__ Unambiguous representation of object,used for debugging,logging etc

    def __repr__(self):
        return ('Employee({},{},{})'.format(self.first, self.last, self.pay))

# __str__ Readable representation of object , used to display for end-user

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Channabasava', 'P', 100000)
emp_2 = Employee('Ned', 'Pierson', 50000)

# print(emp_1.email)
# print(emp_2.email)

# Behaviour is different when you add int or strings
# Depending on the objects , behaviour is different

# print(1+3)
# print('a'+'b')

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# Arithmatic Functions
# print(int.__add__(1, 2))
# print(str.__add__('A', 'N'))


print(emp_1+emp_2)


print(len('Channa'))
print('Channa'.__len__())

print(len(emp_2))
