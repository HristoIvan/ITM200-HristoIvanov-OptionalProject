import csv

with open('data.csv', 'r') as fileCSV:
    fCSV = csv.reader(fileCSV)
    next(fileCSV)
    years = []
    sales = []
    for row in fCSV:
        years.append(int(row[0]))
        sales.append(sum(map(int, row[1:])))
    with open('stats.txt', 'w') as output:
        for year, sale in zip(years, sales):
            if year >= 2012 and year <= 2021:
                output.write(f'{year}: {sale}\n')