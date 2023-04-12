import csv
with open('data.csv', mode = 'r') as fileCSV:
    fCSV = csv.reader(fileCSV)
    for line in fCSV:
        print(line)