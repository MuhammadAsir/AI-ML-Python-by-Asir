#if else
#loop
n=int(input())

inp=input()  #'1 2 3 4 5'
numbers=inp.split()  #['1', '2', '3', '4', '5'] 

po=0;nn=0;e=0;odd=0

for i in range(n):
    a=int(numbers[i])
    print(type(a)) 

    if a > 0:
        po+=1 
    elif a < 0:
        nn+=1
    if a%2==0:
        e+=1
    else:
        odd+=1  
    
print(po,nn,e,odd)    
      


    