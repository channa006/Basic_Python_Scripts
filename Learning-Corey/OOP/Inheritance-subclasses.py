# Inhertance allows us to inherit attributes and methods from parent class
# Create sub-classes and get all the functionality of parent class and overwrit
# Or Add completely new functionality without affecting the parent class


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


class Developer(Employee):
    raise_amount = 1.05

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# emp_1 = Employee('Channa', 'Kalapurmtah', 50000)
# emp_2 = Employee('Shiva', 'Shankar', 60000)


dev_1 = Developer('Channa', 'Kalapurmtah', 50000, 'Python')
dev_2 = Developer('Robert', 'Baratheon', 60000, 'Ruby')

# print(dev_1.email)
# print(dev_2.prog_lang)

mgr_1 = Manager('Rich', 'flower', 70000, [dev_1])
mgr_2 = Manager('Hush', 'Mugabe', 70000, [dev_2])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
print(mgr_1.print_emps())

mgr_1.remove_emp(dev_1)
print(mgr_1.print_emps())

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# Shows details of Class
# print(help(Developer))


print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))


print(issubclass(Developer, Employee))
