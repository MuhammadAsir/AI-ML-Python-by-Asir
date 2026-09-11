txt="My name is Muhammad Asir Hossain Chowdhury"

print(txt,'\n') #\n is used to print in new line

txt2="""My name is Muhammad Asir Hossain Chowdhury,
I am a student of Computer Science and Engineering at EDU.""" #multiline string

print(txt2)

str="HELLO WORLD"
print(str[0]) #indexing starts from 0
x=len(str) #length of string

SLC=str[0:x] #slicing
print(SLC)

a=len(str)#length of string

SLC2=str[0:a:2] #slicing with step
print(SLC2)

SLC3=str[0:a]
print(SLC3[-1]) #negative indexing
print(SLC3[-2])
print(SLC3[-4]) #slicing with negative indexing

print(SLC[::-1]) #reverse string