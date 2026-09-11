
def ARG(*args):
    print(args)

ARG(10,20,30,40,50)

"""*args is used to pass a variable number of arguments to a function. 
It allows you to pass any number of positional arguments to the function, 
and they will be collected into a tuple. 
In the example above, when we call ARG(10,20,30,40,50), 
all the arguments are collected into a tuple and printed as (10, 20, 30, 40, 50)."""


def Kargs(**kwargs):
    print(kwargs)

Kargs(name="Asir",age=20,city="CTG")

#**kwargs is used to pass a variable number of keyword arguments to a function.

#real life usecase of **kwargs
def create_user(**details):
    if "name" in details:
        print("Name:", details["name"])
    if "email" in details:
        print("Email:", details["email"])

create_user(name="Asir", email="asir@gmail.com")