import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
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
print("Forecasting Model Trained Successfully")
future_month = pd.DataFrame({
    'Month_Number': [len(monthly_sales)]
})
predicted_sales = model.predict(future_month)
print("Predicted Sales for Next Month:", predicted_sales[0])