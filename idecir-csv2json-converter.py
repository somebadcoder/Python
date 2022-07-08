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
        if obj[h] == 'null': obj[h] = None

    obj['Id'] = int(obj['Id'])
    obj['Language'] = {}
    for l in ['PT','EN','ES']:
        obj['Language'][l] = obj[l]
        del(obj[l])
        #,'English','Spanish']
    print(json.dumps(obj, indent=2))
