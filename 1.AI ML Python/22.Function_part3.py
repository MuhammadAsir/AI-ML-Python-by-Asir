def add(a,b):
    return a,b

print(type(add(1,2))) # <class 'tuple'>
#So it will return a tuple of (1,2) instead of 3.
# So we need to unzip the tuple to get the values.
x,y=add(1,2)
print(x,y)#so we unzip the tuple to get the values of x and y. 

def add(a,b):
    return [a,b]

print(type(add(1,2))) # <class 'list'>

def add(a,b):
    return {a:b}

print(type(add("age",2))) # <class 'dict'>

