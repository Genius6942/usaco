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
	print(year)

output = ''

fout.write(output + '\n')
fout.close()
print(output)