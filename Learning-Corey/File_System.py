import os

# print(dir(os))
# print(os.getcwd())
# os.chdir('/Users/channp/Documents/Automation/')

# os.mkdir('Demo')
# os.makedirs('Demo\Sub')

# os.rmdir('Demo')
# os.removedirs('Demo\Sub')
# os.stat('Demo')
# os.rename('text.txt','change.txt')

# print(os.getcwd())  - Get current working directory
# print(os.listdir())

# os.chdir('/Users/channp/Documents/Automation/')

# for dirpath, dirnames, filenames in os.walk('/Users/channp/Documents/Automation/'):
#     print('Current Path :', dirpath)
#     print('Directories :', dirnames)
#     print('Files :', filenames)
#     print()

# print(os.environ.get('HOME'))
# # Creating New File in Home Directory\

# filepath = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(filepath)


# print(os.path.basename('/tmp/text.txt'))

# print(os.path.split('/tmp/text.txt'))
# print(os.path.splitext('/tmp/text.txt'))

# Check if Path Exists
# print(os.path.exists('/tmp/text.txt'))


# print(os.path.isdir('/tmp/text.txt'))
# print(os.path.isfile('/tmp/text.txt'))


# 1 - Verify the Directory and Navigatefile_ext
os.chdir('/Users/channp/Documents/Automation/Series')

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    f_name, f_num = file_name.split('_')
    f_num = f_num.strip()[1:].zfill(2)
    print('{}-{}{}' .format(f_num, f_name, file_ext))
