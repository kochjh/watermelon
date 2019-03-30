import matplotlib.pyplot as plt
import csv
with open('../Data/sleepdata.csv', newline='') as f:
	reader = csv.reader(f, delimiter=';')
	l = []
	for actual in reader:
		l.append(actual)
	del l[-1] #delete header
	sq = []
	for x in l:
		x[2] = int(x[2][:-1])#delete percentage char and parse into int
		if int(x[3][:2]) > 3:
			sq.append(x[2])
	plt.plot(sq)
	plt.ylabel('quality of sleep in %')
	plt.xlabel('')
	frame1 = plt.gca()
	frame1.axes.get_xaxis().set_visible(False)
	print("Average sleep quality: ")
	print(sum(sq) / len(sq))
	plt.show()

