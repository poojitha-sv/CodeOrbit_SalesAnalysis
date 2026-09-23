import pandas as pd

# loading the sales data
df = pd.read_csv("sales_data.csv")
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# adding a TotalPrice column since the raw data only has quantity and unit price
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print("Total rows:", len(df))
print()

# 1. total sales
total_sales = df['TotalPrice'].sum()
print("Total Sales: $", round(total_sales, 2))

# 2. average order value
avg_order_value = df['TotalPrice'].mean()
print("Average Order Value: $", round(avg_order_value, 2))

# 3. top products by total sales
print()
print("Top Products by Sales:")
top_products = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)
print(top_products)

# 4. sales by category
print()
print("Sales by Category:")
by_category = df.groupby('Category')['TotalPrice'].sum().sort_values(ascending=False)
print(by_category)

# 5. sales by region
print()
print("Sales by Region:")
by_region = df.groupby('Region')['TotalPrice'].sum().sort_values(ascending=False)
print(by_region)

# 6. sales by month
print()
print("Sales by Month:")
df['Month'] = df['OrderDate'].dt.strftime('%Y-%m')
by_month = df.groupby('Month')['TotalPrice'].sum()
print(by_month)

# saving a summary file with the key numbers
summary = pd.DataFrame({
    'Metric': ['Total Sales', 'Average Order Value', 'Total Orders'],
    'Value': [round(total_sales, 2), round(avg_order_value, 2), len(df)]
})
summary.to_csv('sales_summary.csv', index=False)

top_products.to_csv('top_products.csv')
by_category.to_csv('sales_by_category.csv')
by_region.to_csv('sales_by_region.csv')
by_month.to_csv('sales_by_month.csv')

print()
print("Saved summary files.")
