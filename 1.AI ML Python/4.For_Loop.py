for i in range(10): # for loop will run from 0 to 9 (10 times)
    print(i)


for i in range(1,11): # for loop will run from 1 to 10 (10 times)
    print(i,"Hello World")



sum=0

for i in range(1,11,2): # for loop will run from 1 to 10 with step of 2 (1,3,5,7,9)
    sum=sum+i
    
print("Sum of odd numbers from 1 to 10 is ",sum)


for i in range(5): #nested for loop
   for j in range(5):
       print(i,j)