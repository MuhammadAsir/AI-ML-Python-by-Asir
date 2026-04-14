from functools import reduce 
# reduse is used for performing a cumulative operation on a list of items, such as summing or multiplying them together.

with open("./sample_data/test.txt", "r") as file:
     strings=file.readlines() #it will read the contents of the file and store it in the variable strings
     print(strings)
     TOTAL_LINES=len(strings)
     print(TOTAL_LINES)
     WORDS=list(map(lambda x: len(x.split()),strings)) 
#it will split the contents of the file into words and count the number of words in each line and store it in the variable WORDS
     print(WORDS)
     total_words=reduce(lambda x,y:x+y,WORDS)
     print(total_words)
#cleaning process
     strings=list(map(str.strip,strings))
     print(strings) #deleted newline characters from the end of each line

     strings=list(map(lambda x:x.replace(" ","_"),strings))
     print(strings) #replaced spaces with underscores in each line
     
     strings=list(map(lambda x:len(x),strings))
     print(strings)
     total_char=reduce(lambda x,y:x+y,strings)
     print(total_char)
         
# we will store in another file
     
     with open("./sample_data/test3","w") as file:
          file.write("Total lines: "+str(TOTAL_LINES)+"\n")
          file.write("Total words: "+str(total_words)+"\n")
          file.write("Total characters: "+str(total_char)+"\n")
