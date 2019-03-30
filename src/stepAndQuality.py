import csv
import matplotlib.pyplot as plt

with open('../Data/sleepdata.csv') as csv_file:
	reader = csv.reader(csv_file, delimiter= ';')

	list = []
	for actual in reader:
		list.append(actual)
	del list[-1]
	
	steps = []
	for row in list:
		step = float(row[7])
		steps.append(step)
	
	sq = []
	for x in list:
		x[2] = int(x[2][:-1])#delete percentage char and parse into int
		if int(x[3][:2]) > 3:
			sq.append(x[2])
	
	fig, ax1 = plt.subplots()
	ax1.plot(steps[500:601], color = "yellow")
	ax1.set_ylabel("Number of steps", color="yellow")
	ax2 = ax1.twinx()
	ax2.plot(sq[500:601], color="blue")
	ax2.set_ylabel("Quality of sleep", color="blue")

	plt.xlabel("Entries ordered chonologically")
	
	plt.title ("Number of steps pro day in relation to the sleepingquality", fontsize=14)
	plt.show()