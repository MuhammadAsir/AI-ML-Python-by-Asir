import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah","Sakib"],
    "City": ["New York", "Los Angeles", "Newark", "Boston", "New Delhi", "Chicago", "New Orleans", "Houston","H Los Ang"],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Marketing", "Finance", "HR", "HR"],
    "Salary": [50000, 60000, 55000, 70000, 52000, 58000, 62000, 51000,70000]
}

df = pd.DataFrame(data)
print(df,'\n')

arr1=df.loc[df['City'].str.contains('New',case=False)]
print(arr1,'\n')
#Case false means it will ignore the case of the string while filtering. So it will match "New", "new", "NEW", etc. in the 'City' column.

# starts with Los

arr2=df.loc[df['City'].str.contains(r"^Los")] # ^ using to match the start of the string
print(arr2,'\n')

#ends witk rk
arr3=df.loc[df['City'].str.contains(r"rk$")] # $ using to match the end of the string
print(arr3,'\n')

#starts with a vowel

arr4=df.loc[df['Name'].str.contains(r"^[AEIOU]")] # ^ using to match the start of the string and [AEIOU] to match any vowel
print(arr4,'\n')

arr5=df.loc[df['City'].str.contains(r"New|Los")] # using | to match either "New" or "Los" in the 'City' column
print(arr5,'\n')