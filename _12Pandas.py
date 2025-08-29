import pandas as pd
A = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])  #we can creat our own index 
print(A.values)
print(A.index)
print(A['a'])
print(A['a':'d'])

#Dictionarie
grade_dic = {'A':4,'B':3.5,'C':'fail'}
grade = pd.Series(grade_dic)
print(grade)
print(grade[0:2])

marks_dic = {'A':90,'B':77,'C':'fail'}
marks = pd.Series(marks_dic)
print(marks)

data = pd.DataFrame({"GRADE":grade,"MARKS":marks})
print(data)
print(data.T)
#persentage

# Convert 'MARKS' to numeric, replace non-numeric with NaN
data['MARKS'] = pd.to_numeric(data['MARKS'], errors='coerce')

data['persentage']=data['MARKS']/100
print(data)
data['Age']=[18,19,17] # adding new column
data['NewCol'] = data['Age'] * 2  
# data.drop('NewCol', axis=1, inplace=True)
del data['NewCol']
print(data)
"""
                                       #Creating Data

import pandas as pd

# Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# DataFrame from dict
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# DataFrame from list of lists
df2 = pd.DataFrame([[1, 'A'], [2, 'B']], columns=['Number', 'Letter'])

                                 #Reading and Writing Data

df = pd.read_csv('file.csv')           # Read CSV
df.to_csv('output.csv', index=False)   # Save CSV
df = pd.read_excel('file.xlsx')        # Read Excel
df.to_excel('output.xlsx', index=False)# Save Excel

                                     # Viewing Data

df.head(5)     # First 5 rows
df.tail(5)     # Last 5 rows
df.info()      # Summary of columns & types
df.describe()  # Statistics for numeric columns
df.shape       # (rows, columns)

                                    # Selecting Data

df['Name']            # Single column
df[['Name', 'Age']]   # Multiple columns
df.loc[0]             # Row by label
df.iloc[0]            # Row by position
df.loc[0, 'Name']     # Specific cell
df.iloc[0, 1]         # Specific cell by position

                                    # Filtering Data

df[df['Age'] > 25]          # Rows where Age > 25
df[df['Name'] == 'Alice']   # Rows where Name == 'Alice'
df[(df['Age'] > 25) & (df['Age'] < 35)]  # Multiple conditions

                                    # Modifying Data

df['NewCol'] = df['Age'] * 2         # Add new column
df.drop('NewCol', axis=1, inplace=True)  # Remove column
df.drop(0, axis=0, inplace=True)     # Remove row
df.rename(columns={'Name': 'FullName'}, inplace=True)

                                      #Sorting

df.sort_values(by='Age')              # Sort by Age
df.sort_values(by='Age', ascending=False) # Sort descending

                                      # Aggregation

df['Age'].sum()
df['Age'].mean()
df['Age'].max()
df['Age'].min()
df.groupby('Name')['Age'].mean()  # Group by

                                       # Handling Missing Data

df.dropna()           # Remove rows with NaN
df.fillna(0)          # Replace NaN with 0
df.isnull().sum()     # Count missing values

                                     #  Merging and Joining

pd.concat([df1, df2])                 # Stack DataFrames
pd.merge(df1, df2, on='id')           # Merge on column

"""

# testing real data

import numpy as np 
import pandas as pd 


df = pd.read_excel('D:\sales_records.xlsx')
print(df.head())
#print(df.info()) # info about file data

df2 = df.groupby('Unit Price')[['Total Price','Quantity']].sum().reset_index()
print(df2)