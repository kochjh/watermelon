import matplotlib.pyplot as plt
import csv
with open('../Data/sleepdata.csv', newline='') as f:
	reader = csv.reader(f, delimiter=';')
	l = []
	for actual in reader:
		l.append(actual)
	del l[-1] #delete header
	sq, steps = [],[]
	for x in l:
		x[2] = int(x[2][:-1])#delete percentage char and parse into int
		x[7] = float(x[7])
		if x[7] > 0:
			sq.append(x[2])
			steps.append(x[7])
	plt.plot(sq, steps, 'bs')
	plt.ylabel('quality of sleep in %')
	plt.xlabel('')
	plt.show()

