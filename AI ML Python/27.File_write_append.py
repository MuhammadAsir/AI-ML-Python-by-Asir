#creating and writing a file
with open("./sample_data/test.txt","w") as file:
    file.write("We are learning file handling in python.\n")
    file.write("Let's see how it works.\n")
  

#Append
with open("./sample_data/test.txt","a") as file:
    file.write("Let's goooo.\n")

strings=["Python is a great language.\n",] 
with open("./sample_data/test2.txt","a") as file:
    file.writelines(strings)
     
print(file.closed)