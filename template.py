"""
ID: mathman5
LANG: PYTHON3
TASK: test
"""

import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

problemName = "test"

fin = open(os.path.join(__location__, problemName + '.in'), 'r')
fout = open(os.path.join(__location__, problemName + '.out'), 'w')
data = fin.read().splitlines()
# your awesome code here

output = ''

fout.write(output + '\n')
fout.close()
print(output)