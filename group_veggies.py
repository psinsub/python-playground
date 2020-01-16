#by Poupae and Uzair

# Read vegtables.csv into a variable called vegtables.
from pprint import pprint
import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    vegetables = [dict(row) for row in rows] # Convert OrderedDict to regular dict

# # Group vegtables by color as a vegetable vegtables_by_color.
vegetable_by_color= {}
for x in vegetables:
    color = x['color']
    if color in vegetable_by_color:
        vegetable_by_color[color].append(x)
    else:
        vegetable_by_color[color] = [x]

# # Output vegtables_by_color into a json called vegtables_by_color.json.
import json

with open('vegetable_by_color.json', 'w') as f:
    json.dump(vegetable_by_color, f, indent=4)