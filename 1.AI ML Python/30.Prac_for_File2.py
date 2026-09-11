with open("./sample_data/write_read.txt","w+") as file: #w+ is for write and read both
    file.write("This is the first line.\n")

    print(file.tell())
    print(file.read())
    file.seek(0)

    file.truncate(5)
#truncate() method is used to cut the file content from the specified position. 
    print(file.read())