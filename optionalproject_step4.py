with open('data.csv') as f:
    lines = [line.strip().split(',') for line in f.readlines()]

header = lines[0]
data = lines[1:]

sales_2021 = [int(sale) for sale in data[-2][1:7]]
sales_2022 = [int(sale) for sale in data[-1][1:7]]

total_sales_2021 = sum(sales_2021)
total_sales_2022 = sum(sales_2022)

sgr = (total_sales_2022 - total_sales_2021) / total_sales_2022

with open('stats.txt', 'w') as f:
    f.write(f'Sales growth rate: {sgr:.10f}')

estimated_sales_2022 = []
for i in range(7, 13):
    sale_2021 = int(data[-2][i])
    estimated_sale_2022 = sale_2021 + sale_2021 * sgr
    estimated_sales_2022.append(estimated_sale_2022)

with open('stats.txt', 'a') as f:
    f.write('\n\nEstimated sales for the last 6 months of 2022:\n')
    for month, sale in zip(header[7:], estimated_sales_2022):
        f.write(f'{month}: {sale:.0f}\n')