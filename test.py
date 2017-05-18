import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.disable(logging.DEBUG)
logging.info('Start of program')

def range_of_list(the_list):
	logging.info("Range is %s counts long" % len(the_list))


def equals(a,b,c,d,e):
	if len(set(map(len, (a, b, c, d)))) == 1 and len(a) - 1 == len(e):
		logging.info("Lists are equal!")
	else:
		raise Exception('Unequal_Lists')

def length(a,b,c,d,e):
	print("\nLength test failed!")
	print("%s,%s,%s,%s,%s" % (len(a),len(b),len(c),len(d),len(e)))

def hoc_thousand(counts):
	if counts != 1000:
		raise Exception("HoC does not equal 1000!")
	else:
		logging.info('HoC is equal to 1000')

def in_order(body):
	for i in range(len(body)):
		if i != 0:
			num = int(body[i].replace(',', ''))
			if start - num == 1:
				start = num
			else:
				logging.info("Out Of Order:: Prev: %s Current: %s" % (start,num))
				start = num
		else:
			start = int(body[0].replace(',', ''))