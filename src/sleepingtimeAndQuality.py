import matplotlib.pyplot as plt
import numpy as np
import csv

def qualityAsInt(quality):
	return int(quality[:-1])

def getStartingHour(row):
	return int(row[1][:2])
	
with open('../Data/sleepdata_weekday_correct.csv', newline='') as f:
	reader = csv.reader(f, delimiter=';')
	l = []
	for actual in reader:
		l.append(actual)
	del l[-1] #delete header
	days, counter = [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
	days2, counter2 = [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
	for x in l:
		if int(x[6][:2]) > 3:
			if x[2] != "Freitag" and x[2] != "Samstag":
				if getStartingHour(x) == 20:
					days[0] += qualityAsInt(x[5])
					counter[0] += 1
				elif getStartingHour(x) == 21:
					days[1] += qualityAsInt(x[5])
					counter[1] += 1
				elif getStartingHour(x) == 22:
					days[2] += qualityAsInt(x[5])
					counter[2] += 1
				elif getStartingHour(x) == 23:
					days[3] += qualityAsInt(x[5])
					counter[3] += 1
				elif getStartingHour(x) == 0:
					days[4] += qualityAsInt(x[5])
					counter[4] += 1
				elif getStartingHour(x) == 1:
					days[5] += qualityAsInt(x[5])
					counter[5] += 1
				elif getStartingHour(x) == 2:
					days[6] += qualityAsInt(x[5])
					counter[6] += 1
				else:
					days[7] += qualityAsInt(x[5])
					counter[7] += 1
			else:
				if getStartingHour(x) == 20:
					days2[0] += qualityAsInt(x[5])
					counter2[0] += 1
				elif getStartingHour(x) == 21:
					days2[1] += qualityAsInt(x[5])
					counter2[1] += 1
				elif getStartingHour(x) == 22:
					days2[2] += qualityAsInt(x[5])
					counter2[2] += 1
				elif getStartingHour(x) == 23:
					days2[3] += qualityAsInt(x[5])
					counter2[3] += 1
				elif getStartingHour(x) == 0:
					days2[4] += qualityAsInt(x[5])
					counter2[4] += 1
				elif getStartingHour(x) == 1:
					days2[5] += qualityAsInt(x[5])
					counter2[5] += 1
				elif getStartingHour(x) == 2:
					days2[6] += qualityAsInt(x[5])
					counter2[6] += 1
				else:
					days2[7] += qualityAsInt(x[5])
					counter2[7] += 1
	print(days)
	days[0] /= counter[0]
	days[1] /= counter[1]
	days[2] /= counter[2]
	days[3] /= counter[3]
	days[4] /= counter[4]
	days[5] /= counter[5]
	if counter[6] != 0:
		days[6] /= counter[6]
	if counter[7] != 0:
		days[7] /= counter[7]
	print(days)
	
	if counter2[0] != 0:
		days2[0] /= counter2[0]
	days2[1] /= counter2[1]
	days2[2] /= counter2[2]
	days2[3] /= counter2[3]
	days2[4] /= counter2[4]
	days2[5] /= counter2[5]
	if counter2[6] != 0:
		days2[6] /= counter2[6]
	if counter2[7] != 0:
		days2[7] /= counter2[7]
		
	n_groups = 8
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8
	
	rects1 = plt.bar(index, days, bar_width,
	alpha=opacity,
	color='b',
	label='weekdays')
	 
	rects2 = plt.bar(index + bar_width, days2, bar_width,
	alpha=opacity,
	color='g',
	label='weekend')
	 
	plt.xlabel('starttime of sleep')
	plt.ylabel('avg. sleep quality in %')
	plt.xticks(index + bar_width / 2, ('20:00-20:59', '21:00-21:59', '22:00-22:59', '23:00-23:59', '00:00-00:59', '01:00-01:59', '02:00-02:59', '03:00-19:59'))
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
	

