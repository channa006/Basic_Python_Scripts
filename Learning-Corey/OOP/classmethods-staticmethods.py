# Regular Method and Class, Automatically takes instance as first Argument.
# By Convention we call it as self

# Change this begaviour , instead take class as first Argument
# To do that we use class method


import datetime


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Channa', 'Kalapurmtah', 50000)
emp_2 = Employee('Shiva', 'Shankar', 60000)

Employee.set_raise_amt(1.05)


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Berlin-Moore-7000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_2.email)
print(new_emp_2.pay)

# Static Methods - don't pass anything by default


my_date = datetime.date(2020, 5, 15)

print(Employee.is_workday(my_date))
