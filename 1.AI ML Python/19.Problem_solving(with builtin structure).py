
lst=[10,20,30,40,50,10,20,50,60,70,80,90,100]
unique_values=set(lst)#cast the list into set to get unique values only
#set is a built in data structure which is used to store unique values only
lst=list(unique_values)
print(lst)


str="hello world welcome to python programming, welcome to python programming.Data science is a good career option"
word=str.split()
print(word,'\n')


count={}#empty dictionary

for i in word:
    count[i]=count.get(i,0)+1 
#get method is used to get the value of the key,
#if the key is not present in the dictionary then it will return the default value which is 0 in this case, 
#and then we are adding 1 to it to count the frequency of each word in the string

print(count,'\n')


for k,v in count.items():
    print(k,v)
