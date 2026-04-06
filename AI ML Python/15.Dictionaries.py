#Dictionaries is a data structure that stores data in key-value pairs. 
#It is also known as a hash map or associative array in other programming languages.
#In Python, dictionaries are created using curly braces {} and key-value pairs are separated by a colon :
#It is also unordered, meaning that the items in a dictionary do not have a specific order.
#key must be unique and immutable.ex: int,string, number, tuple
#value can be of any data type and can be duplicated.
student={}
print(type(student), '\n')

student = {"name": "Asir", "age": 20, "grade": "A","numbers":[1,2,3]}
#In this example, name, age, and grade are the keys
#"Asir", 20, and "A" are the corresponding values.
print(student, '\n')

#accessing values in a dictionary

print(student["name"],'\n')
#Or print(student.get("name"),'\n')

#Adding or updating key-value pairs in a dictionary
student["age"] = 25 #update
print(student, '\n')    

print(student.get("math"),'\n')
#This will print None because the key "math" does not exist in the dictionary.

print(student.get("math",0),'\n')
#This will print 0 because the key "math" does not exist in the dictionary,
#and we have provided a default value of 0 to return when the key is not found.
