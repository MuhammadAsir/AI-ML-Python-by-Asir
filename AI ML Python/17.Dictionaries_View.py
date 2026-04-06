my_dict={"name":"Asir","age":20,"grade":"A"}
keys=my_dict.keys()
print(keys, '\n')

val=my_dict.values()
print(val, '\n')

#items method returns a view object that 
#displays a list of dictionary's key-value tuple pairs.
items=my_dict.items()
print(items, '\n')

#items view is dynamic, meaning that it reflects changes made to the dictionary.
for i,j in my_dict.items():
    print(i,j)


