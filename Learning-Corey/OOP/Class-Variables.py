# Class Variables are variables that are shared among all instances of Class

# Instances Var can be unique to Instances.Class Var are same for each Instance


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


emp_1 = Employee('Channa', 'Kalapurmtah', 50000)
emp_2 = Employee('Shiva', 'Shankar', 60000)

print(Employee.num_of_emps)

# print(emp_1.fullname())
# print('Current Pay', emp_1.pay)
# emp_1.apply_raise()
# print('New Pay', int(emp_1.pay))

# print(emp_2.fullname())
# print('Current Pay', emp_2.pay)
# emp_2.apply_raise()
# print('New Pay', int(emp_2.pay))


# Significance of self.raise_amount
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# Print Name Space
# print(emp_1.__dict__)
# print(Employee.__dict__)

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
