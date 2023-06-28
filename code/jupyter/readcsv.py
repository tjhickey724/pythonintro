import csv

with open('code/jupyter/people.csv', 'r') as csvfile:
    people = list(csv.DictReader(csvfile,delimiter=","))
print(len(people))

# clean data, make age and height integers
for person in people:
    person['age']= int(person['age'])
    person['height'] = int(person['height'])

# create a list of the people who are too old (>120) or too young (<0)

for person in people:
    print(person)


    


