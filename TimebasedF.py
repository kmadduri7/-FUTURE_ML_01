import pandas as pd
df = pd.read_excel(r"C:\Users\m yadaiah\Desktop\S&D\Online Retail.xlsx.xlsx")

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Day'] = df['InvoiceDate'].dt.day

print(df.head())

monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['Sales'].sum()

monthly_sales = monthly_sales.reset_index()
monthly_sales['InvoiceDate'] = monthly_sales['InvoiceDate'].astype(str)

