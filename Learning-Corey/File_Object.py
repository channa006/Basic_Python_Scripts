# File Objects
import os
# f = open('Demo.txt', 'r')
# print(f.name)
# print(f.mode)
# for i in f:
#    print(i.strip())
# f.close()

# File Context Manager

os.chdir('/Users/channp/Code/Basic_Python_Scripts/Learning-Corey/')
with open('Demo.txt', 'r') as f:
   f_contents = f.read()
   print(f_contents)

# Show all the lines readlines , single line readline
# with open('Demo.txt', 'r') as f:
#     for i in f:
#         print(i, end='')

# f_contents = f.readline()
#     print(f_contents, end= '')

# Read all contents of the File
# with open('Demo.txt', 'r') as f:
#     size_to_read = 10

#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

# # set the position back to 0

#     f.seek(0)

#     f_contents = f.read(size_to_read)
#     print(f_contents)

# while len(f_contents) > 0:
#     print(f_contents, end='*')
#     f_contents = f.read(size_to_read)
#     print(len(f_contents))

# with open('Demo.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

# with open('Demo.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)


# with open('Demo.txt', 'r') as r:
#     with open('Demo_write.txt', 'w') as w:
#         for line in r:
#             w.write(line)

# JPEG Files Copying
# with open('Demo.jpg', 'rb') as r:
#     with open('Demo_write.jpg', 'wb') as w:
#         for line in r:
#             w.write(line)

# with open('Demo.txt', 'rb') as r:
#     with open('Demo_write.txt', 'wb') as w:
#         chunk_size = 4096
#         r_chunk = r.read(chunk_size)

#         while len(r_chunk) > 0:
#             w.write(r_chunk)
#             r_chunk = r.read(chunk_size)
