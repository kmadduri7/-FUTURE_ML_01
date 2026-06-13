import pandas as pd
import numpy as np
df = pd.read_excel(r"C:\Users\m yadaiah\Desktop\S&D\Online Retail.xlsx.xlsx")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Sales'] = df['Quantity'] * df['UnitPrice']
monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['Sales'].sum()
monthly_sales = monthly_sales.reset_index()
monthly_sales['Month_Number'] = np.arange(len(monthly_sales))
print(monthly_sales.head())