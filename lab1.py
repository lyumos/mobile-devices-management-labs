import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

ac = len(sys.argv)
if (ac != 2):
	print("Usage : python3 lab2.py DUMP_FILE")
	exit()
traffic = 0.0
f = open(sys.argv[1])
i = 0
x = []
y = []
for line in f.readlines():
	if len(line.split("217.15.20.194")) == 1:
		continue
	x.append(line.split()[1])
	try:
		traffic += float(line.split()[-2])
		y.append(float(line.split()[-2]))
	except ValueError:
		traffic += float(line.split()[-3]) * 1024.0 * 1024
		y.append(float(line.split()[-3]) * 1024.0 * 1024)
traffic /= 1024
traffic -= 1000
coord = zip(x, y)
sorted_coord = sorted(coord, key=lambda tup: tup[0])
x_sorted = [coord[0] for coord in sorted_coord]
y_sorted = [coord[1] for coord in sorted_coord]
fig, ax = plt.subplots()
ax.vlines(x_sorted, 0, y_sorted, linewidth=2.0)
ax.xaxis.set_major_locator(ticker.MultipleLocator(80))
ax.yaxis.set_major_locator(ticker.MultipleLocator(2000000))
ax.grid(which='major')
ax.set_title('Итоговая стоимость для ip "217.15.20.194" - ' + str(int(traffic)) + " p.", fontsize=25)
ax.set(ylabel='TRAFFIC, BYTES', xlabel='TIME')
ax.xaxis.label.set_size(20)
ax.yaxis.label.set_size(20)
ax.tick_params(axis='both', which='major', labelsize=12)
plt.show()
