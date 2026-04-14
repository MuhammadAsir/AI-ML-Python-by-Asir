#map(function, iterable)
#It means: Apply this function to every item in the list

lst=[1,2,3,4]

cube=list(map(lambda x:x**3,lst))
print(cube)


# Why list()? map() does NOT return a list directly
# It returns a map object (like a generator)
# If you want a list, you need to convert it using list() function