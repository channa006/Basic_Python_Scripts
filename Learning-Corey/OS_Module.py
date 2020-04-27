# Allows us to interact with underlying OS in several different ways.

import os
from datetime import datetime

# print(os.__file__)
# print(dir(os))

# print(os.getcwd())

# Change the File system path
# os.chdir('/Users/channp/Documents/Automation/')

# Get Print Working Directory
# print(os.getcwd())

# os.mkdir('Demo')

# List Directories
# print(os.listdir('/Users/channp/Documents/Automation/Learning'))

# Nested Folders can be created
# os.makedirs("Demo")

# Remove Directories
# os.rmdir('')
# os.removedirs('')


# Rename Files/Directory
# os.rename('Test.txt','Demo.txt')

# OS File Stats


# print(os.getcwd())
# print(os.stat('Demo.txt'))

# print(os.stat('Demo.txt').st_size)

# Last Modified time
#mod_time = os.stat('Demo.txt').st_mtime

# Readable time format
# print(datetime.fromtimestamp(mod_time))

# Traverse and print the Folder/Subfolder/Files

# for dirpath, dirnames, filenames in os.walk('/Users/channp/Documents/Automation/'):
#    print('Current Path:', dirpath)
#    print('Directories :', dirnames)
#    print('Files :', filenames)
#    print()


# Print the ENV Variable , Home Folder

os.chdir('/Users/channp/Desktop')

#print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

print(file_path)
