file =open("./sample_data/sample.txt","r")
content = file.readlines()
content=list(map(str.strip,content)) #removing extra lines and spaces
filter_content=list(filter(lambda x:len(x)>=1,content)) #removing empty lines

print((filter_content))
   
print(file.closed) 
#checking file is closed or not.Always we have to check that otherwise we have to face data leakage

#to avoid data leakage we have to close the file after using it
file.close()
print(file.closed)

#best way to handle file is using with statement

with open("./sample_data/sample.txt","r") as file:
  for line in file:
   print(line,end="") #removing extra lines

print(file.closed)

#for store: for line in file: l=line.strip()