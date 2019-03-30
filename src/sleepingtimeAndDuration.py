import matplotlib.pyplot as plt
import numpy as np
import csv

def durationAsInt(duration):
	h = int(duration[:2])
	min = int(duration[3:5])
	return h * 60 + min

def getStartingHour(row):
	return int(row[1][:2])
	
with open('../Data/sleepdata_weekday_correct.csv', newline='') as f:
	reader = csv.reader(f, delimiter=';')
	l = []
	for actual in reader:
		l.append(actual)
	del l[-1] #delete header
	days, counter = [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
	for x in l:
		if int(x[6][:2]) > 3:
			if x[2] != "Freitag" and x[2] != "Samstag":
				if getStartingHour(x) == 20:
					days[0] += durationAsInt(x[6])
					counter[0] += 1
				elif getStartingHour(x) == 21:
					days[1] += durationAsInt(x[6])
					counter[1] += 1
				elif getStartingHour(x) == 22:
					days[2] += durationAsInt(x[6])
					counter[2] += 1
				elif getStartingHour(x) == 23:
					days[3] += durationAsInt(x[6])
					counter[3] += 1
				elif getStartingHour(x) == 0:
					days[4] += durationAsInt(x[6])
					counter[4] += 1
				elif getStartingHour(x) == 1:
					days[5] += durationAsInt(x[6])
					counter[5] += 1
				elif getStartingHour(x) == 2:
					days[6] += durationAsInt(x[6])
					counter[6] += 1
				else:
					days[7] += durationAsInt(x[6])
					counter[7] += 1
					
	print(days)
	days[0] /= counter[0]
	days[1] /= counter[1]
	days[2] /= counter[2]
	days[3] /= counter[3]
	days[4] /= counter[4]
	days[5] /= counter[5]
	if days[6] != 0:
		days[6] /= counter[6]
	if days[7] != 0:
		days[7] /= counter[7]
	print(days)
	n_groups = 8
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8
	
	rects1 = plt.bar(index, days, bar_width,
	alpha=opacity,
	color='b',
	label='avg. sleep duration in min')
	 
	rects2 = plt.bar(index + bar_width, counter, bar_width,
	alpha=opacity,
	color='g',
	label='number of start sleeping in ')#fix name
	 
	plt.xlabel('starttime of sleep')
	plt.ylabel('')
	plt.xticks(index + bar_width, ('20:00-', '21:00-', '22:00-', '23:00-', '0:00-', '01:00-', '02:00-', '03:00-'))
	plt.legend()
	 
	plt.tight_layout()
	plt.show()
#0 =  20:00-20:59
#1 = 21:00-21:59
#2 = 22:00-22:59
#3 = 23:00-23:59
#4 = 00:00-00:59
#5 = 01:00-01:59
#6 = 02:00-02:59
#7 = 03:00-19:59
	

