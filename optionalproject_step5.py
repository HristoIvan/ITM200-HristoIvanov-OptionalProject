import matplotlib.pyplot as plt

with open('stats.txt', 'r') as file:
    data = file.readlines()

sales = []
for line in data:
    if line.startswith('Jul:'):
        sales.append(int(line.split(':')[1]))
    elif line.startswith('Aug:'):
        sales.append(int(line.split(':')[1]))
    elif line.startswith('Sep:'):
        sales.append(int(line.split(':')[1]))
    elif line.startswith('Oct:'):
        sales.append(int(line.split(':')[1]))
    elif line.startswith('Nov:'):
        sales.append(int(line.split(':')[1]))
    elif line.startswith('Dec:'):
        sales.append(int(line.split(':')[1]))

fig, ax = plt.subplots()
ax.barh(['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], sales)

ax.set_xlabel('Estimated Sales of Vehicles')
ax.set_ylabel('Month')
ax.set_title('Estimated Sales of Vehicles in Canada, for the Last 6 Months of 2022')

plt.show()