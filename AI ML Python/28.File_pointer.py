with open("./sample_data/sample.txt", "r") as file:
    print(file.tell())#Tell() is used to find the current position of the file pointer.
    print(file.read())#Read() is used to read the contents of the file. After reading the file, the file pointer will be at the end of the file.
    print(file.tell())
    print('\n')
with open("./sample_data/sample.txt", "r") as file:
     print(file.read(5))#it will read first 5 characters of the file
     print(file.tell()) #pointer will be at 5
     print(file.read()) #it will read the remaining characters of the file
     print(file.tell())#pointer will be at the end of the file

print('\n')
#seek is used to move the file pointer to a specific position in the file.

with open("./sample_data/sample.txt", "r") as file:
     print(file.tell())
     print(file.read())
     print(file.tell())
     file.seek(0)#it will move the file pointer to the beginning of the file
     print(file.tell())#pointer will be at the beginning of the file
     print(file.read())#it will read the contents of the file again