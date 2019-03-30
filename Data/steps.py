import csv
import matplotlib.pyplot as plt

#plt.plot([1, 2, 3, 4, 4])
#plt.ylabel('some numbers')
#plt.show()

sleepfile = 'sleepdata.csv'
with open(sleepfile) as csv_file:
	reader = csv.reader(csv_file, delimiter= ';')

	list = []
	for actual in reader:
		list.append(actual)
	del list[-1]
	
	steps = []
	
	for row in list:
		if float(row[7]) > 0:
			step = float(row[7])
			steps.append(step)
	
	plt.plot(steps)
	plt.xlabel("Timeline")
	plt.ylabel("Number of steps")
	
	plt.title ("Number of steps pro day")
	plt.show()

