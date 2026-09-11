def gen(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]



lst=[1,2,3,4,5,6,7,8]
x=gen(lst,3)
print(next(x))
print(next(x))
print(next(x))