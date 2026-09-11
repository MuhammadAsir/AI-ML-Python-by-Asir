#def is a keyword to define a function
def my_func():
    print("HELLO")

my_func()#calling the function


def print_name(name):
    print(f"My name is {name}",'\n')

print_name("Asir")


def default_para(name="Asir"):
    print(f"My name is {name}",'\n')
default_para("Muhammad")#it will take default value

def add(a,b):
    """This function will add two numbers"""

    return a+b

sum=add(10,2)
print(sum)

help(add) #it will give the information about the function
