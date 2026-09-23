# Sales Data Analysis Report

## About the Dataset
I used a small sample sales dataset (sales_data.csv) with 20 orders. It has columns for OrderID, OrderDate, Product, Category, Region, Quantity, and UnitPrice, covering January and February 2024. I added a TotalPrice column (Quantity x UnitPrice) since that wasn't in the raw data.

## Tool Used
Python 3 with pandas (analyze_sales.py).

## Key Metrics

**Total Sales:** $1,647.24
**Average Order Value:** $82.36
**Total Orders:** 20

## Top Products by Sales
1. Office Chair - $539.94
2. Wireless Mouse - $319.80
3. Desk Lamp - $315.00
4. Bluetooth Speaker - $270.00
5. Notebook Set - $202.50

Office Chair is the top-selling product even though it wasn't ordered the most times - this is because it has a high price per unit ($89.99), so a small number of orders still added up to the highest total.

## Sales by Category
- Furniture: $854.94
- Electronics: $589.80
- Stationery: $202.50

Furniture brings in the most revenue overall, mainly because of Office Chair and Desk Lamp both being higher-priced items.

## Sales by Region
- East: $478.90
- North: $471.92
- South: $462.42
- West: $234.00

The East, North and South regions are all fairly close to each other in sales, but the West region is noticeably behind the others.

## Sales by Month
- January 2024: $870.87
- February 2024: $776.37

Sales were a bit higher in January than February in this sample.

## Summary
Based on this data, Office Chair and the Furniture category are the strongest performers, and the West region is the weakest, so that could be an area to focus on. Since this is a small sample dataset, these patterns are just for practice, but the same approach (grouping by product, category, region, and time) would work the same way on a bigger real dataset.
