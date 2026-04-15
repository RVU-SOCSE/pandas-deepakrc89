import pandas as pd


df = pd.read_csv('C:/Users/deepa/Downloads/mcd.csv')


print("Original DataFrame:")
print(df)


print("\nMissing values in each column:")
print(df.isnull().sum())


df_filled = df.fillna(df.mean(numeric_only=True))


print("\nDataFrame after filling missing values with mean:")
print(df_filled)
