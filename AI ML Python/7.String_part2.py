#Splitting, Joining, Formatter String
str="Welcome to Python Programming, Python is a great language to learn."

print(str.split(),'\n') #tokenizes the string into a list of substrings

str2="Hello,Welcome to my world."
print(str2.split(),'\n') #tokenizes based on whitespace
print(str2.split(","),'\n')# tokenizes based on comma


token=str.split()

token="-".join(token)
#joins the list of substrings into a single string with the specified separator
print(token,'\n')

name="John"
age=30
height=5.92131

print(f"My name is {name}. I am {age} years old and my height is {height:.3} feet.",'\n')
#f-string is a way to format strings in python

accuracy=0.8999332
print(f"The model accuracy is {accuracy: .2%}",'\n')
#formats the number as a percentage with 2 decimal places