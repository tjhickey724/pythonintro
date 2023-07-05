import csv
with open('code/courses/courses.csv','r',encoding='UTF-8') as infile:
    data = list(csv.DictReader(infile))
print(len(data))
print(data[1000])

c1 = data[1000]
for k in c1:
    print(k,c1[k])


i_study = [d for d in data if d['independent_study']=='True' and d['enrolled']!='0']
print('independent studies with at least one student',len(i_study))
