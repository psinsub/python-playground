#by Poupae and Uzair

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#read in the csv file

import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict

#print the variable vegetables

print(vegetables)

#Write vegetables as a JSON file called vegetables.json
import json

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent=4)