import pandas as pd

data = {
    'Name': ['Aman', 'Riya', 'Karan', 'Sneha'],
    'Marks': [75, 85, 65, 90]
}

df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)


df['Total Marks'] = df['Marks'] + 5


print("\nDataFrame after adding new column:")
print(df)
