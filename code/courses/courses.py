import csv
with open('code/courses/courses.csv','r') as infile:
    data = list(csv.DictReader(infile))
print(len(data))
