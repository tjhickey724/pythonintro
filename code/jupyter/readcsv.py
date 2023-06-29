import csv

with open('code/jupyter/people.csv', 'r') as csvfile:
    people = list(csv.DictReader(csvfile, delimiter=","))

def clean_data():
    for person in people:
        person['age'] = int(person['age'])
        person['height'] = int(person['height'])
        person['age_in_weeks'] = person['age'] * 52  
clean_data()

for person in people:
    print(person)