"""
ID: mathman5
LANG: PYTHON3
TASK: gift1
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')
data = fin.read().replace('_' , ' ').splitlines()

np = int(data[0]) # number of people

names = data[1 : np + 1]
people = {}
for name in names:
	people[name] = 0 # key: name, value: money they have

line = np + 1
output = []
for _ in range(np):
	name = data[line]
	moneyData = data[line + 1].split(' ')
	giving = int(moneyData[0])
	numPeople = int(moneyData[1])
	if numPeople <= 0:
		people[name] += giving
		continue
	moneyGiving = giving // numPeople
	moneyKeeping = giving % numPeople
	people[name] += moneyKeeping - giving
	for i in range(numPeople):
		people[data[line + 2 + i]] += moneyGiving
	line += numPeople + 2

for name in names:
	output.append(name + ' ' + str(people[name]))

output = '\n'.join(output)

fout.write(output + '\n')
fout.close()
print(output)