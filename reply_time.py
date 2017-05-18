import numpy as np
import re
from copy import copy
from datetime import datetime

def one_count_int(time_reverse):
	time_end = []
	time_start = []

	for x in range(len(time_reverse)):
		if x == 0:
			time_end.append(time_reverse[x])
		elif x == len(time_reverse) - 1:
			time_start.append(time_reverse[x])
		else:
			time_end.append(time_reverse[x])
			time_start.append(time_reverse[x])

	np_time_end = np.array(time_end)
	np_time_start = np.array(time_start)
	diff = np_time_end - np_time_start


	time_diff = re.compile(r'(\d\d):(\d\d)\.(\d\d\d\d\d\d)')
	new_diff = []

	for d in diff:
		str_d = str(d)
		new = time_diff.search(str_d)
		
		new1 = new.group(1)
		new2 = new.group(2)
		new3 = new.group(3)

		if int(new1) == 0:
			new_group = "%s.%s" % (new2,new3)
			new_num = float(new_group)
		else:
			new_group = "%s:%s.%s" % (new1,new2,new3)
			new_num = datetime.strptime(new_group, '%M:%S.%f')

		new_diff.append(new_num)

	return diff, new_diff

def overall_time(time):
	end = time[0]
	start = time[-1]

	overall = end - start
	
	file = open('stats.txt', 'a')
	file.write("##Reply Times\n\n")
	file.write("*Times in Seconds*\n\n")
	file.write("**Total Time: %s**\n\n" % overall)

	file.close()


def build_diff_list(time,intr):
	loops = int((len(time)-1)/intr + 1)

	time_list = []

	for i in range(loops):
		if i == 0:
			time_list.append(time[i])
		else:
			time_list.append(time[i * intr])

	later = np.array(time_list[:-1])
	earlier = np.array(time_list[1:])

	diff = later - earlier

	return diff



def row_output(diff, intr, file, loops, sub = False, ref = ""):
	for i in range(loops):

		total_seconds = diff[i].total_seconds()
		minutes = (total_seconds % 3600) // 60

		time = diff[i]

		sec = diff[i].seconds
		micro = diff[i].microseconds

		if sub:
			for j in range(len(diff)):
				if ref[j] == time:
					mult = j
		else:
			mult = i


		start = mult * intr
		end =  (mult+1) * intr

		if minutes == 0:
			file.write('%s-%s|%s.%s\n' % (start,end,sec,micro))
		else:
			file.write('%s-%s|%s:%s.%s\n' % (start,end,minutes,sec,micro))



def table_output(diff, intr, file_name):
	
	if file_name == 'splits.txt' and intr == 100:
		file = open('%s' % file_name, 'w')
	else:
		file = open('%s' % file_name, 'a')

	file.write("\n\n###%s Splits\n\n" % intr)
	file.write('Range | Time |\n:--- | :--- |\n')


	loops = int(len(diff))
	row_output(diff, intr, file, loops)

	file.close()

def fast_n_slow(diff, intr):
	diff_sort = np.sort(diff)

	file = open('stats.txt', 'a')

	file.write("\n\n###Fastest & Slowest %s count split\n\n---\n\n" % intr)
	
	file.write('\n\n####Fastest 5\n\n')
	file.write('Range | Time |\n:--- | :--- |\n')

	loops = 5
	row_output(diff_sort, intr, file, loops, True, diff)


	file.write('\n\n####Slowest 5\n\n')
	file.write('Range | Time |\n:--- | :--- |\n')

	diff_flip = np.flipud(diff_sort)
	row_output(diff_flip, intr, file, loops, True, diff)

	file.close()


def split(time,intr):
	diff = build_diff_list(time,intr)

	if intr == 100:
		table_output(diff, intr, 'stats.txt')
		table_output(diff, intr, 'splits.txt')
	else:
		table_output(diff, intr, 'splits.txt')
		fast_n_slow(diff, intr)

	
