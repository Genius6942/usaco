"""
ID: mathman5
LANG: PYTHON3
TASK: ride
"""

from math import prod


fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
read = fin.read().splitlines()
comet = read[0]
ride = read[1]
isRide = prod([ord(char.lower()) - 96 for char in ride]) % 47 == prod([ord(char.lower()) - 96 for char in comet]) % 47
output = ''
if isRide:
	output = 'GO'
else:
	output = 'STAY'
output += '\n'
fout.write(output)
fout.close()