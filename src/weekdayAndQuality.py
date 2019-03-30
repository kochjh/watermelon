import matplotlib.pyplot as plt
import numpy as np
import csv

def qualityAsInt(quality):
	return int(quality[:-1])

with open('../Data/sleepdata_weekday_correct.csv', newline='') as f:
	reader = csv.reader(f, delimiter=';')
	l = []
	for actual in reader:
		l.append(actual)
	del l[-1] #delete header
	days, counter = [0,0,0,0,0,0,0],[0,0,0,0,0,0,0]
	for x in l:
		if int(x[6][:2]) > 3:
			if x[2] == "Montag":
				days[0] += qualityAsInt(x[5])
				counter[0] += 1
			if x[2] == "Dienstag":
				days[1] += qualityAsInt(x[5])
				counter[1] += 1
			if x[2] == "Mittwoch":
				days[2] += qualityAsInt(x[5])
				counter[2] += 1
			if x[2] == "Donnerstag":
				days[3] += qualityAsInt(x[5])
				counter[3] += 1
			if x[2] == "Freitag":
				days[4] += qualityAsInt(x[5])
				counter[4] += 1
			if x[2] == "Samstag":
				days[5] += qualityAsInt(x[5])
				counter[5] += 1
			if x[2] == "Sonntag":
				days[6] += qualityAsInt(x[5])
				counter[6] += 1				
	days[0] /= counter[0]
	days[1] /= counter[1]
	days[2] /= counter[2]
	days[3] /= counter[3]
	days[4] /= counter[4]
	days[5] /= counter[5]
	days[6] /= counter[6]
	
	print(days)
	
	n_groups = 7
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8
	
	rects1 = plt.bar(index, days, bar_width,
	alpha=opacity,
	color='b',
	label='avg. sleep quality in %')
	 
	rects2 = plt.bar(index + bar_width, counter, bar_width,
	alpha=opacity,
	color='g',
	label='amount of measures')
	 
	plt.xlabel('')
	plt.ylabel('')
	plt.xticks(index + bar_width, ('mondays', 'tuesdays', 'wednesdays', 'thursdays', 'fridays', 'saturdays', 'sundays'))
	plt.legend()
	 
	plt.tight_layout()
	plt.show()
#0 =  Montag
#1 = Dienstag
#2 = Mittwoch
#3 = Donnerstag
#4 = Freitag
#5 = Samstag
#6 = Sonntag
	

