#Method of Dictionaries

my_dict = {"name": "Asir", "age": 20, "grade": "A"}
print(my_dict, '\n')

#Adding a new key-value pair to the dictionary
my_dict["Math Marks"]=97
print(my_dict, '\n')

my_dict["name"]="Muhammad Asir"
print(my_dict, '\n')


del my_dict["Math Marks"]
print(my_dict, '\n')

dic_2=my_dict.copy()
print(dic_2, '\n')

dic_3={(10,20,30):"A"}
print(dic_3, '\n')  
#It is possible to use a tuple as a key in a dictionary because tuples are immutable,
#meaning they cannot be changed after they are created. 
#This makes them hashable, which is a requirement for dictionary keys. 
#In contrast, lists are mutable and cannot be used as dictionary keys because their contents can change, making them unhashable.
