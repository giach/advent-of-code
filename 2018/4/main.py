import re, fileinput, operator
from collections import defaultdict

def main():
	# each entry has 0 as default value
	total_time = defaultdict(int)
	sleeping_time = defaultdict(lambda: defaultdict(int))

	input_txt = sorted(fileinput.input())

	for line in input_txt:

		# parse the minute
		minute = int(re.search(r':(\d+)', line).group(1))
		if "#" in line:
			# parse the guard ID
			guard = int(re.search(r'#(\d+)', line).group(1))
		if "falls" in line:
			m0 = minute
		if "wakes" in line:
			m1 = minute
			for m in range(m0, m1):
				total_time[guard] += 1
				sleeping_time[guard][m] += 1

	# sort by value and get element with the greatest value
	sleepy_guard, _ = sorted(total_time.items(), key=operator.itemgetter(1))[-1]
	golden_minute, _ = sorted(sleeping_time[sleepy_guard].items(), key=operator.itemgetter(1))[-1]
	print ("Part 1:", sleepy_guard * golden_minute)

	sleepy_minutes = defaultdict(int)
	for guard in sleeping_time:
		sleepy_minutes[guard] = sorted(sleeping_time[guard].items(), key=lambda a: a[1])[-1]

	# determine the values to compare using the lambda function
	sleepy_guard_2, (sleepy_min, _) = max(sleepy_minutes.items(), key=lambda a: a[1][1])
	print("Part 2:", sleepy_guard_2 * sleepy_min)


main()
