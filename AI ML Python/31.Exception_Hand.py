#Exception Handling: Errors that occur during the execution of a program.

n=int(input())
try:
    a=10/n
except ZeroDivisionError:
   print("ERROR!!!")
else:
    print(a)    



try:
    x=y
except ZeroDivisionError:
    print("ERROR!!!")
except NameError as e:
    print(e)


try:
    file=open("./sample_data/file.txt","r") 
    file.read()
except FileNotFoundError as e:
    print(e)
else:
    print(File.read())
finally:
    print("This will always be executed")
     

