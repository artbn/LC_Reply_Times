import numpy as np
from copy import copy
import re
import test

def header(body):
	file = open('stats.txt', 'w')
	file.write('#Reply Time Stats\n\n#%s-%s\n\n' % (body[-1],body[0]))
	file.close()


def footer():
	file = open('stats.txt', 'a')
	file.write('\n\n --- \n\nFor errors or suggestions contact /u/artbn')
	file.close()



def five_stats(my_list):
	median = np.median(my_list)
	average = np.average(my_list)
	std = np.std(my_list)
	MAX = np.amax(my_list)
	MIN = np.amin(my_list)
	return median, average, std, MAX, MIN

def overall_stats(diff):
	np_diff = np.array(diff)

	median, average, std, MAX, MIN = five_stats(np_diff)

	file = open('stats.txt', 'a')

	file.write("\n\n##Overall Stats\n\n")
	file.write("*Times are in seconds*\n\n")
	file.write("Median: %s\n\n" % median)
	file.write("Maximum: %s\n\n" % MAX)
	file.write("Minimum: %s\n\n" % MIN)
	file.write("Average: %s\n\n" % average)
	file.write("Standard Deviation: %s\n\n" % std)


	file.close()

def ind_stats(author,diff):
	names = set(author)
	names_list = list(names)

	new_author = copy(author)
	del new_author[-1]
	np_names = np.array(new_author)

	np_diff = np.array(diff)

	file = open('stats.txt', 'a')
	file.write('##Individual Stats\n\n')
	file.write('*Times are in seconds*\n\n')
	file.write('Username | Median | Max | Min | Average | Standard Deviation |\n:---: | :---: | :---: | :---: | :---: | :---: |\n')

	for name in names_list:
		time_list = np_diff[np_names == name]
		median, average, std, MAX, MIN = five_stats(time_list)

		file.write('%s|%s|%s|%s|%s|%s\n' % (name, median, MAX, MIN, average, std))

	file.close()

def fast_five(ID,body,author,diff):
	np_diff = np.array(diff)
	diff_sort = np.sort(np_diff)

	np_ID = np.array(ID)
	np_ID = np_ID[:-1]

	np_body = np.array(body)
	np_body = np_body[:-1]

	np_author = np.array(author)
	np_author = np_author[:-1]


	file = open('stats.txt', 'a')
	file.write('\n\n##Fastest 5 times\n\n')
	file.write('*Times are in seconds*\n\n')
	file.write('ID | Count | Username | Reply Time |\n:---: | :---: | :---: | :---: |\n')

	#Finds and outputs fastes 5 reply times
	for i in range(5):
		diff_o = diff_sort[i]

		# Removes the brackets and ' from the element. Element is matched with the position based on fastest reply time
		ID_o = re.sub("[\[''\]]", '', np.array_str(np_ID[diff_o == np_diff]))
		body_o = re.sub("[\[''\]]", '', np.array_str(np_body[diff_o == np_diff]))
		author_o = re.sub("[\[''\]]", '', np.array_str(np_author[diff_o == np_diff]))

		file.write('%s|%s|%s|%s\n' % (ID_o, body_o, author_o, diff_o))

	file.close()

def hoc(author_list):
	
	author = author_list[:-1]

	unique, counts = np.unique(author, return_counts=True)
	hoc_dict = dict(zip(unique, counts)) 

	import operator

	#Sorts from low to high
	sorted_hoc = sorted(hoc_dict.items(), key=operator.itemgetter(1)) 
	sorted_hoc.reverse()

	file = open('stats.txt', 'a')
	file.write('\n\n##HoC\n\n')
	file.write('Username | Count |\n:---: | :---: |\n')

	counts = 0 #Used to test if 1000

	for i in range(len(sorted_hoc)):
		name = sorted_hoc[i][0]
		count = sorted_hoc[i][1]
		counts += count
		file.write("%s|%s\n" % (name, count))

	try:
		test.hoc_thousand(counts)
	except:
		print("Error: This program was created for reply times for 1000 counts. \n This error means that you are either trying to use this program for other than 1000 counts or there are duplicate or missing counts in the range selected!")