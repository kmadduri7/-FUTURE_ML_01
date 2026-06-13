import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel(r"C:\Users\m yadaiah\Desktop\S&D\Online Retail.xlsx.xlsx")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Sales'] = df['Quantity'] * df['UnitPrice']
monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['Sales'].sum()
monthly_sales = monthly_sales.reset_index()
plt.plot(monthly_sales['InvoiceDate'].astype(str),
         monthly_sales['Sales'])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()