even=[]
for i in range(21):
    if i%2==0:
        even.append(i)

print(even,'\n')


random_list=[x for x in range(21) if x%2==0]#List comprehension
print(random_list,'\n')

list=[i*3 for i in range(5)]#it's multiplying each element by 3 and storing in list
print(list,'\n')

#Now we will do List comprehension with list of strings

fruits=['apple','banana','grapes','orange']
capital_fruits=[]

for fruit in fruits:
    capital_fruits.append(fruit.capitalize())
 #capitalize() is used to convert the first letter of the string to uppercase 

print(capital_fruits,'\n')   

upper_fruits=[fruit.upper() for fruit in fruits]
#upper() is used to convert the string to uppercase
print(upper_fruits,'\n')