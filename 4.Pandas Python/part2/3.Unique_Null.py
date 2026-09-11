import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"],
    "City": ["New York", "London", "Paris", "New York", "Tokyo", "London"],
    "Score": [85, 90, 78, 85, 95, 90]
}

df = pd.DataFrame(data)
#unique means distinct values in a column and nunique means number of distinct values in a column
# unique works on only series 
df['Name'].unique()
print("Unique Names:", df['Name'].unique())

df1=pd.read_csv('student_data.csv')
print(len(df1['Data Structure Marks'].unique())) #ds unique marks length,it has counted the null value also. 
print(df1['Data Structure Marks'].nunique()) #nunique of ds marks, it has not counted the null value.
print(df.nunique()) #nunique of all columns

#Check NULL
print(df1.isnull()) #it will give true for null values and false for non null values

print(df1['Data Structure Marks'].hasnans) #it will give true if there is any null value in the column otherwise it will give false