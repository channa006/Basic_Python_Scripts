
student = {'Name': 'John', 'Age': '18', 'courses': ['Maths', 'Social'], 'Phone': '888-9898'}
# print(student)

# Print only the value for key
print(student['Name'])

# Alternate using method
# print(student.get('courses'))


# Updating the Key and Value
# student['Phone'] = '888-89876'
# print(student.get('Phone'))


# If jey don't exist returns "Not found"
# print(student.get('hone', "Not Found"))

# Update all in one shot
# student.update({'Name': 'Randy', 'Age': '28', 'Courses': ['Vedic', 'Social'], 'Phone': '555-5555'})
# print(student)

# Delete Specific Key and Value
# del student['Age']
# print(student)

# We can use the pop functions
# age = student.pop('Age')
# print(student['Age'])
# print(student)

# Check the Number of keys in the dictionary
# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())


# For loop, Below will loop over the Key
# for key in student:
#     print(key)

# For Loop , Below will loop over the Key and Value
# for key, value in student.items():
#     print(key, value)
