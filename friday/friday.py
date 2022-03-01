"""
ID: mathman5
LANG: PYTHON3
TASK: test
"""

import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

problemName = "friday"

fin = open(os.path.join(__location__, problemName + '.in'), 'r')
fout = open(os.path.join(__location__, problemName + '.out'), 'w')

years = int(fin.read())

start = 1900
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for year in range(start, start + years):
	for month in range(len(months)):
		days = 0
		if month == 1: # febuary leap year yay
			if year % 100 == 0:
				if year % 400 == 0:
					days = 29
				else:
						days = 28
			elif year % 4 == 0:
				days = 29
			else:
				days = 28
		else:
			days = months[month]
		
						

output = ''

fout.write(output + '\n')
fout.close()
print(output)