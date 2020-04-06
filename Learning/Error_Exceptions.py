# How to handle Error and Exceptions

# try:
#     f = open('Demo.txt', 'r')
#     for line in f:
#         print(line, end='')
# except Exception:
#     print('Sorry , This File does not Exist')


# try:
#     f = open('Dem.txt', 'r')
#     for line in f:
#         print(line, end='')
# except FileNotFoundError:
#     print('Sorry , This File does not Exist')

# try:
#     f = open('Demo.txt', 'r')
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     # for line in f:
#     #     print(line, end='')
# finally:
#     print('Executing....')

# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass


try:
    f = open('Demo.txt', 'r')
    if f.name=="Demo.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Errr")
else:
    print(f.read())
    # for line in f:
    #     print(line, end='')
finally:
    print('Executing....')
