import re
import uuid
import datetime


def uuid_time(ID):

	uuid_str = re.search('\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', ID).group(0)

	# pull out time field
	time_field = uuid.UUID(uuid_str).time


	# divide time into a unix timestamp and microsecond remainder
	timestamp = (time_field - 0x01B21DD213814000) // 10000000

	usecs = (time_field % 10000000) // 10

	# combine them into a UTC datetime
	time_obj = datetime.datetime.fromtimestamp(timestamp) + datetime.timedelta(microseconds=usecs)

	return time_obj


def uuid_difference(time_obj, time_obj2):
	return time_obj - time_obj2

