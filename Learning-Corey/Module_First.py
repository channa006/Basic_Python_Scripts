
"""
When Python Runs the File, Before Running any code it sets the few special var
__name__ is one of the special vaiable
It sets __name__ = __main__
"""


# def main():
#     print("First Module : {}". format(__name__))
#
#
# if __name__ == '__main__':
#     main()


if __name__ == '__main__':
    print('Run Directly')
else:
    print('Run from Import')
