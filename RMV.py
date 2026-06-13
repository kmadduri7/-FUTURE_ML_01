import pandas as pd

# Load dataset
df = pd.read_excel(r"C:\Users\m yadaiah\Desktop\S&D\Online Retail.xlsx.xlsx")

# Remove missing values
df.dropna(inplace=True)

# Remove cancelled orders
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# Convert InvoiceDate to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create Sales column
df['Sales'] = df['Quantity'] * df['UnitPrice']

# Show output
print(df.head())