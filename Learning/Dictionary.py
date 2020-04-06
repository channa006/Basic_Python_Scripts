
student = {'name': 'John', 'Age': '18', 'courses': ['Maths','Social'],'Phone':"888-9898" }
#print(student)

#Print only the value for key
#print(student['name'])

#Alternate using method
#print(student.get('courses'))


#Updating the Key and Value 
#student['phone'] = '8888'

#If jey don't exist returns "Not found"
#print(student.get('phone',"Not Found"))

#Update all in one shot 
#student.update({'name': 'Rand', 'Age': '28', 'courses': ['Vedic','Social'],'Phone':'555-5555'})
#print(student)

#Delete Specific Key and Value
#del student['Age']
#print(student)

#We can use the pop functions 
#age = student.pop('Age')
#print(age)
#print(student)

#Check the Number of keys in the dictionary 
#print(len(student))
#print(student.keys())
#print(student.values())
#print(student.items())


#For loop, Below will loop over the Key 
#for key in student:
#    print(key)
    
#For Loop , Below will loop over the Key and Value
#for key,value in student.items():
#    print(key,value)