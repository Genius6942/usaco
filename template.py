"""
ID: mathman5
LANG: PYTHON3
TASK: test
"""

fin = open('test.in', 'r')
fout = open('test.out', 'w')
data = fin.read().splitlines()
# your awesome code here

output = ''
if True:
	output = 'YES'
else:
	output = 'NO'

fout.write(output + '\n')
fout.close()
print(output)