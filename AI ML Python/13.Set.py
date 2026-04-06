#Set is an built in data type in Python that is used to store unique elements. 
#It is an unordered collection of items, 
#which means that the items do not have a specific order and cannot be accessed by index. 
#Sets are mutable, which means that you can add or remove elements from a set after it has been created.
#indexing and slicing are not supported in sets because they are unordered collections.

st={1,2,3,4,5}
print(type(st),st,'\n')

st1={}
print(type(st1)) #This is not a set, it's a dictionary.
#To create an empty set, we need to use the set() function.
st1=set()
print(type(st1)) #set

st2=()
print(type(st2)) #tuple

st3=[]
print(type(st3)) #list

S={1,2,3,4,5,5,5}
if 5 in S:
    print("5 is present in the set S")

S1={5,2,3,1,4}
print(S1) #It's changed the order of the elements because sets are unordered collections.


#S1.append(6) ,AttributeError: 'set' object has no attribute 'append'
S1.add(6) #To add an element to a set, we can use the add() method.
S1.add(10) 
print(S1)

S1.pop() #The pop() removes the first element from the set.Answer:2,3,4,5,6,10
print(S1)

S1.remove(10)
print(S1)
