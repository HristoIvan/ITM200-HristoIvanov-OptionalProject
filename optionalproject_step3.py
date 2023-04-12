import csv
import matplotlib.pyplot as plt

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

years = [int(row[0]) for row in data[1:-1]]
sales_data = [[int(s) for s in row[1:]] for row in data[1:-1]]

total_sales = [sum(sales) for sales in sales_data]

plt.bar(years, total_sales)
plt.xlabel('Year')
plt.ylabel('Total Vehicles Sold in Canada, in Millions')
plt.title('Total Sales of Vehicles in Canada, by Years 2012-2021')
plt.show()