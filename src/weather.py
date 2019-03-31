import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

file = '../Data/weatherdata2.csv'
with open(file) as csv_file:
	reader = csv.reader(csv_file, delimiter= ',')

	list = []
	for actual in reader:
		list.append(actual)
	del list[0]
	
	temperature = []
	for row in list: 
		if len(row) > 5:
			temp = row[5]
			if len(temp) > 0:
				if temp[0] == '-':
					temperature.append(-float(temp[1:]))
				else:
					temperature.append(float(temp))
			
	
	plt.plot(temperature)
	plt.ylabel("Temperature")
	plt.xlabel("Timeline in hours")
	plt.show()