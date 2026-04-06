str="Welcome to Python Programming, Python is a great language to learn."

print("Length of String",len(str))
print("String in Uppercase",str.upper())
print("String in Lowercase",str.lower())

processed_str=str.lower()

print("python" in processed_str) 
#finds the substring in the string and returns true or false

print(str.capitalize())
#capitalizes the first letter of the string and converts the rest to lowercase

print(str.find("Python"))#finds the first occurrence of the substring in the string 

print(str.rfind("Python"))#finds the last occurrence of the substring in the string

cnt=str.count("Python")
print(cnt)

RPLC=str.replace("Python","Java")
print(RPLC) #wont change the original string as strings are immutable in python

txt="HELLO,WELCOME TO MY WORLD."
print(txt.endswith(".")) 
#checks if the string ends with the specified character or substring