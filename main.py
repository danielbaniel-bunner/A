import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
df = pd.read_excel('/Users/momo/A/account.xls')

# This will display the first few rows of the file
print(df.head())
