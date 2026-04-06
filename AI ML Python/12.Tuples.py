#Tuples is a collection of data which is ordered and unchangeable. 
#In Python tuples are written with round brackets.

tup=(1,2,3,4,5)

print(type(tup),tup,"\n")

mixed_tuples=(1,2,"Hello",True,3.14) #we can store different data types in a tuple.
print(type(mixed_tuples),mixed_tuples)

tup1=(1)
print(type(tup1),tup1) #This is not a tuple, it's an integer.

tup1=(1,) 
#To create a tuple with a single element, we need to add a comma after the element.

lst=[10,20,30]

tup2= tuple(lst) #We can convert a list to a tuple using the tuple() function.
print(type(tup2),tup2)

print(tup2[0]) #We can access elements of a tuple using indexing.

tup3=mixed_tuples[0:3] #slicing a tuple
print(tup3)

#immutable nature of tuples
#tup2[0]=100 ,This will raise an error because tuples are immutable.
#tup2.append(40) #This will also raise an error because tuples do not have an append method.

#tuple methods

tup4=(5,10,15,20,25,5,5,5)
print(tup4.count(5)) 
#count() method returns the number of times a specified value appears in the tuple.

print(tup4.index(15))