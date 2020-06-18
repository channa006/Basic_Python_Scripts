# Lists

courses = ['Maths', 'Science', 'Social', 'Computer', 'Geography']
courses_new = ['Pysics', 'Chemistry']
nums = [1, 6, 2, 7, 8, 3]

# print(courses)
# print(len(courses))


# Indexing
# print(courses[0])
# print(courses[1])
# print(courses[2])
# print(courses[3])
# print(courses[4])

# Negative Index
# print(courses[-1])

# Range Index
# print(courses[0:3])
# print(courses[2:])

# Append to List
# courses.append('Arts')
# courses.remove('Maths')
# courses.insert(1, 'Arts')

# Remove the last Item in the List. i.e Geography
popped = courses.pop()
print(popped)
print(courses)
# print(courses_new)

# Merging two Lists
# courses.extend(courses_new)
# print(courses)


# Sorting the Lists
# courses.reverse()
# print(courses)

# courses.sort()
# print(courses)

# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)


# Sorted version of lists without altering actual Position
# sorted_nums = sorted(nums)
# print(sorted_nums)
#
# print(min(nums))
# print(max(nums))
# print(sum(nums))


# Search Functions for Lists
# print(courses.index('Geography'))
# print('Maths' in courses)

# for item in courses:
#     print(item)

# for index, course in enumerate(courses):
#     print(index, course)

# for index, course in enumerate(courses, start=2):
#     print(index, course)

# Lists to Strings - Join Method
# course_str = ' , '.join(courses)
# print(course_str)

# course_str = ' - '.join(courses)
# print(course_str)

# # Strings to Lists
# new_list = course_str.split('-')
# print(new_list)


# Lists are Mutable , Tuples are Immutable
# Mutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)

# Tuples - Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# tuple_1[0] = 'Art'
#
# print(tuple_1)
# print(tuple_2)

# Sets - Doesn't show the duplicate Values

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# print(cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
cs_courses_1 = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(cs_courses_1))
print(cs_courses.union(cs_courses_1))

# Empty Lists
# empty_list = []
# empty_list = list()

# Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# Empty Sets
# empty_set = {} # This isn't right! It's a dict
# empty_set = set()
