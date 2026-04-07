#Iterator
s={10,20,30,40,50,60}
# print(s[0]), will give error because set is unordered collection of unique elements
#Sets don't support indexing, slicing, or other sequence-like behavior.

s=iter(s) # we can create an iterator from the set using the iter() function
print(next(s))
print(next(s))
print(next(s))
#It is not ordered, so the output will be different every time we run the code.


#Generator is a special type of iterator that is defined using a function.
#It allows us to create an iterator that can be iterated over one value at a time, 
#without the need to store all the values in memory at once. 
#This is useful when we are working with large datasets 
# or when we want to generate an infinite sequence of values.

lst=[i for i in range(500)]
print()
def data(chunk_size,lst):
    for i in range(0,len(lst),chunk_size):
        yield lst[i:i+chunk_size]

x=data(5,lst)
print(type(x)) # <class 'generator'>

print(next(x))
print(next(x))