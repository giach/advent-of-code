import re
from datetime import datetime, time, timedelta

# def get_date(time):


def fix_date(time):
	# strip the [] parentheses
	date = time[0][1:]
	hour = time[1][:-1]

	# parse the date
	dd = [int(dx) for dx in date.split("-")]
	d = datetime(dd[0], dd[1], dd[2])


	# parse the hour and increse the time by 1 day
	# in case the hour is before midnight
	hh = hour.split(":")
	hh = [int(hx) for hx in hh]
	td = timedelta(days=0, hours=hh[0], minutes=hh[1])
	if hh[0] != 0:
		td = timedelta(days=1)

	d = d + td

	return "{:%Y-%m-%d %H:%M}".format(d)

def main():
	dates = {}
	guards_asleep_time = {}

	with open('input') as file:
		lines = file.readlines()

	for line in lines:
		# match everthing inside []
		tmp = re.findall("\\[.*\\]", line)
		time = tmp[0].split(" ")
		time = fix_date(time)

		# match evething afer ]
		action = re.findall("(?<=\\] ).*$", line)

		date = time.split(" ")[0]
		hour = time.split(" ")[1]

		action.append(hour)
		if date in dates:
			dates[date].append(action)
		else:
			dates[date] = [action]

	for key in dates:
		sleep = 0
		# print(key, dates[key])
		for action in dates[key]:
			# the action. eg falls asleep, wakes up, begins shift
			act = action[0]
			# the time of the action. eg: 00:03. keep just the minutes
			act_time = int(action[1].split(":")[1])
			# the amount of time the guard sleeps during his shift

			if 'falls' in act:
				sleep -= act_time
			if 'wakes' in act:
				sleep += act_time
			if 'Guard' in act:
				guard_nr = re.findall("#[0-9]*", act)[0][1:]

		if guard_nr in guards_asleep_time:
			old_asleep_time = guards_asleep_time[guard_nr]
			new_asleep_time = old_asleep_time + sleep
			guards_asleep_time[guard_nr] = new_asleep_time
		else:
			guards_asleep_time[guard_nr] = sleep

	most_asleep_min = 0
	sleepy_guard = 0
	for key in guards_asleep_time:
		if most_asleep_min < guards_asleep_time[key]:
			most_asleep_min = guards_asleep_time[key]
			sleepy_guard = key

	print("The sleepyiest guard is ")
	print(sleepy_guard, most_asleep_min)


	tmp = []
	for key in dates:
		for action in dates[key]:
			if sleepy_guard in action[0]:
				tmp.append(key)
				continue

	minutes = []
	intervals = []

	for t in tmp:
		minutes = []
		for action in dates[t]:
			if "Guard" not in action[0]:
				hour = action[1]
				minute = int(hour.split(":")[1])
				minutes.append(minute)

		minutes = sorted(minutes)
		print(minutes)
		while minutes:
			p1 = minutes[0]
			p2 = minutes[1]
			intervals.append([p1,p2])
			minutes = minutes[2:]
	print(intervals)

	r, c = 60, 60

	matrix = [[0 for i in range(0,r)] for j in range(0,c)]
	index = 0
	for interval in intervals:
		r_start, r_end = interval
		while r_start < r_end:
			matrix[r_start][index] = 1
			r_start += 1
		index += 1

	print (matrix[1])
	sums = [sum(matrix[i]) for i in range(0,r)]


	golden_minute = 40
main()
