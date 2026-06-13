import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
df = pd.read_excel(r"C:\Users\m yadaiah\Desktop\S&D\Online Retail.xlsx.xlsx")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Sales'] = df['Quantity'] * df['UnitPrice']
monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['Sales'].sum()
monthly_sales = monthly_sales.reset_index()
monthly_sales['Month_Number'] = np.arange(len(monthly_sales))
X = monthly_sales[['Month_Number']]
y = monthly_sales['Sales']
model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)
print("MAE:", mean_absolute_error(y, predictions))
print("MSE:", mean_squared_error(y, predictions))