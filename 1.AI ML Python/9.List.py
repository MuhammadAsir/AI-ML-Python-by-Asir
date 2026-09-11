arr=[1,2,3,4,5,6,7,8,9,10]

print(type(arr),'\n')

new_list=arr[0:5]
print(new_list,'\n')

arr.append(11)
print(arr,'\n')

arr.insert(0,100)
print(arr,'\n')

arr.pop()
print(arr,'\n')

arr.remove(100)
print(arr,'\n')

nested_list=[[10,20,30],[40,50,60],[70,80,90]] #nested list
print(nested_list,'\n')

print(nested_list[0][2],'\n')

print(max(arr),'\n')
print(min(arr),'\n')

mx=max(arr)
print(arr.index(mx),'\n')#index of max element
