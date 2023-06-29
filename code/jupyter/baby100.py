import csv
#import matplotlib.pyplot as plt

babyfile = open("code/jupyter/baby100.csv","r",encoding="utf-8")
data = list(csv.DictReader(babyfile,delimiter=','))
babyfile.close()

for d in data:
    d['year']=int(d['year'])
    d['count'] = int(d['count'])
    d['percent'] = float(d['percent'])
    d['rank']=int(d['rank'])

rank1names = [d['name'] for d in data if d['rank'] == 1]

print(rank1names)
print(set(rank1names))