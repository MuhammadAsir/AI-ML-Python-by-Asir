import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"],
    "City": ["New York", "London", "Paris", "New York", "Tokyo", "London"],
    "Score": [85, 90, 78, 70, 95, 90]
}

df = pd.DataFrame(data)

print(df.duplicated()) #it will give true for duplicate rows and false for non duplicate rows
print("Number of duplicated values:",df.duplicated().sum()) #it will give the count of duplicate rows

# delelting duplicates values 
print(df.drop_duplicates())#it will delete the duplicate rows and keep only one row for each duplicate value

#deletes permanently the duplicate values from the dataframe
df.drop_duplicates(inplace=True)
print(df)

#Deletes duplicate values based on specific columns

print(df.drop_duplicates(subset=['Name']) )#it will delete the duplicate rows based on the 'Name' column and keep only one row for each duplicate value in the 'Name' column
print(df.drop_duplicates(subset=['Name'],keep="last") )#it will keep the last occurrence of the duplicate value and delete the previous occurrences