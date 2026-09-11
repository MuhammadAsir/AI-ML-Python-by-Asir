"""Write a function introduce(name, age) that prints:

 My name is <name> and I am <age> years old.
 
Call it using positional arguments.

Sample Input:
Rhim 28

Sample Output:
My name is Rahim and I am 28 years old."""

def func(name,age):
    print(f"My name is {name} and I am {age} years old.")


n,a=input().split()
func(n,a)