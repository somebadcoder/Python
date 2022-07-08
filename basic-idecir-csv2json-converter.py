import sys, json, time 
filename = 'new-test.csv'
with open(filename) as f: 
    lines = f.readlines()
    headers = lines[0].strip().split(',')

for index, line in enumerate(lines):
    if index == 0:
        continue
    obj = {}
    for i,h in enumerate(headers):
        obj[h] = line.split(',')[i].strip()
        obj['Id'] = int(obj['Id'])
    print(obj)
