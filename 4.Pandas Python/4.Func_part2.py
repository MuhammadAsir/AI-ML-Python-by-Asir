import pandas as pd 

my_list = [['Alice', 25], ['Bob', 30], ['Charlie', 28]]

list_df=pd.DataFrame(my_list,columns=['Name','Age'],index=[1,2,3])
print(list_df,'\n')

my_tuple = (('Alice', 25), ('Bob', 30), ('Charlie', 28))

tuple_df = pd.DataFrame(my_tuple,columns=['Name','Age'])

print(tuple_df,'\n')


my_dictionary={'Name':['Alice', 'Bob', 'Charlie'],'Age':[25, 30, 28]}

dict_df = pd.DataFrame(my_dictionary,columns=['Name','Age'])
print(dict_df,'\n')


my_data=[{'Name':'Alice','Age':25,'City':'New York'},{'Name':'Bob','Age':30,'City':'Los Angeles'},
         {'Name':'Charlie','Age':28}]
data_df = pd.DataFrame(my_data,columns=['Name','Age','City'])
print(data_df)