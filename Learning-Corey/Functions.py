# Functions are basically set of instructions packaged together, which performs specific task.


# def hello_fun():
#     print("Hello Function")
#
#
# hello_fun()

# Allow us to put the code in single location with sole purpose.
# DRY - Don't Repeat Yourself
# Machine , Take the input and Produce the output
# Python Scope - In Detail - Future , Want to know the scope of variables etc
# Passing an Argument

def hello_fun(greeting):
    return '{} Function'.format(greeting)


print(hello_fun('Hello'))

# Passing multiple Argument

# def hello_fun(greeting, name):
#    return '{} {}'.format(greeting, name)
# print(hello_fun('Hello', 'Darling'))

# Second Argument not passed

# def hello_fun(greeting, name="You"):
#    return '{} {}'.format(greeting, name)

# print(hello_fun('Hello', "Romeo"))

# Allowing us to accept arbitary number of positional or keyword arguments.
# student_info function takes Classes a student is taking , plus the keyword argument will be random information about the student.
# you can see in both eg we don't know how many positional and keyword arguments will be.
# That's why we use *arg , **kwargs


# def student_info(*args, **kwargs):
#    print(args)
#    print(kwargs)

#student_info('Maths', 'Sciene', 'Social', name='Yasmine', age='24')

# OncePrined
#args = Tuples
#kwargs = dictioanry

#('Maths', 'Sciene', 'Social')
#{'age': '24', 'name': 'Yasmine'}


# Unpack and send the values using * and **

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# course = ['Maths', 'Sciene', 'Social']
# student = {'age': '24', 'name': 'Yasmine'}
#
# student_info(*course, **student)
