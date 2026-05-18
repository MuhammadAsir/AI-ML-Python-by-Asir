#We have to dowload  ip install openpyxl for reading excel file
"""
🔥 One-line difference
CSV → simple text tables (Best for: basic data storage & sharing)
Excel → formatted spreadsheet (Best for: human-readable reports & analysis)
Parquet → fast big data storage (Best for: large datasets & analytics)
JSON → structured (nested) data format (Best for: APIs & semi-structured data)
"""
import pandas as pd 

import pandas as pd 

df=pd.read_csv('student_data.csv') 
print("CSV file")
print(type(df),'\n',df)

print('\n')

excel_file = pd.read_excel('phitron_student_marks.xlsx')
print("Excel file")
print(excel_file)
print(type(excel_file))

print('\n')
#parquet file

parquet_file = pd.read_parquet('students.parquet')
print("Parquet file")
print(parquet_file)

print(type(parquet_file))

print('\n')

# json file

json_file = pd.read_json('data.json')
print("Json file")
print(json_file)

print(type(json_file))

print('\n')