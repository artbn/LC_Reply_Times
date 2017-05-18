import json
import re
import numpy as np

import uuid_time
import test
import stats
import reply_time


last_file = open("C:/xampp/htdocs/mainthreadstats/data/lastChatFile.txt")
last_file_num = last_file.read()


for i in range(int(last_file_num)+1):
	file = open("C:/xampp/htdocs/mainthreadstats/data/chat%s.json" % i, encoding='utf-8')
	if i == 0:
		data = json.load(file)
	else:
		data += json.load(file)
		print('File #%s loaded' % i)


def ask_input():
	start = input("Start: ")
	end = input("\nEnd: ")
	collect(start,end)


def collect(start,end):

	loop = False

	id_reverse = []
	body_reverse = []
	author_reverse = []
	time_reverse = []


	number = re.compile(r'(\d)?\D*(\d\d\d)\D*(\d\d\d)')


	for line in data:
		ID = line['id']
		body = line['body']
		author = line['author']
		stricken = line['stricken']

		num_body = number.search(body)


		if ID == end:
			loop = True

		if loop and not stricken and num_body != None:
			
			id_reverse.append(ID)

			time = uuid_time.uuid_time(ID)
			time_reverse.append(time)

			author_reverse.append(author)

			n1 = num_body.group(1)
			n2 = num_body.group(2)
			n3 = num_body.group(3)

			if n1:
				num = "%s,%s,%s" % (n1,n2,n3)
			else:
				num = "%s,%s" % (n2,n3)

			body_reverse.append(num)

		if ID == start:
			loop = False


	test.range_of_list(id_reverse)

	test.in_order(body_reverse)

	stats.header(body_reverse)

	#Calculate one count intervals
	diff, new_diff = reply_time.one_count_int(time_reverse)


	#Testing
	try:
		test.equals(body_reverse, id_reverse, author_reverse, time_reverse, diff)
	except:
		test.length(body_reverse, id_reverse, author_reverse, time_reverse, diff)



	#Full Table Output
	file = open('time.txt', 'w')

	for body, ID, author, time, newer_diff in zip(body_reverse, id_reverse, author_reverse, time_reverse, new_diff):
		file.write("%s|%s|%s|%s|%s\n" % (ID, body, author, time, newer_diff)) 

	file.close()

	#Reply Times
	reply_time.overall_time(time_reverse)
	reply_time.split(time_reverse,100)
	reply_time.split(time_reverse,20)
	reply_time.split(time_reverse,5)

	#Stats
	stats.overall_stats(new_diff)
	stats.ind_stats(author_reverse,new_diff)
	stats.fast_five(id_reverse,body_reverse,author_reverse,new_diff)
	stats.hoc(author_reverse)


	#Testing
	try:
		test.equals(body_reverse, id_reverse, author_reverse, time_reverse, diff)
	except:
		test.length(body_reverse, id_reverse, author_reverse, time_reverse, diff)

	stats.footer()


if __name__ == "__main__":
	ask_input()